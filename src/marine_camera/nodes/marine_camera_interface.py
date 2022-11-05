#!/usr/bin/env python3
#from asyncio.windows_events import NULL
import struct
import time
import socket
import av
import cv2
import io
import numpy as np
import os
import threading
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
class marine_camera_node():
    def __init__(self):

        self.image_pub = rospy.Publisher("image_topic_2",Image,queue_size=10)
        self.bridge = CvBridge()
        self.mcast_group_ip = '239.100.1.112'
        self.mcast_group_port = 20502
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.local_ip = socket.gethostbyname(socket.gethostname())
        self.sock.bind(('', self.mcast_group_port))

        self.mreq = struct.pack("=4sl", socket.inet_aton(self.mcast_group_ip), socket.INADDR_ANY)
        self.sock.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP,self.mreq)

        self.cnt=0
        self.rawData = io.BytesIO()
        self.container = av.open(self.rawData, format="h264", mode='r')
        
        self.cur_pos = 0

        self.pack_initial_total = 0
        self.pack_initial_id = 0
        self.frame_total = b''

        self.img=None
    def read_data(self):
        while True:
            try:
                data, addr = self.sock.recvfrom(65535)
                #print(f'{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}: Receive data from {addr}')
                #print('id:', data[4] + data[5] * 256 + data[6] * 256 * 256 + data[7] * 256 * 256 * 256)
                #print('type:', type(data))
                #print('total', data[8] + data[9] * 256)
                #print('num', data[10] + data[11] * 256)
                # if data[12] + data[13] * 256!=1440:
                #     print('youxiao', data[12] + data[13] * 256)
                #     print(data.hex())
                pack_num = data[10] + data[11] * 256
                #print("1")

                if  pack_num == 0:
                    pack_initial_total = data[8]+data[9]*256
                    pack_initial = data[32:]
                    pack_initial_id = data[4]+data[5]*256+data[6]*256*256+data[7]*256*256*256
                    frame_total = pack_initial
                else:

                    #print("2")
                    pack_total_2 = data[8] + data[9] * 256
                    pack_id = data[4] + data[5] * 256 + data[6] * 256 * 256 + data[7] * 256 * 256 * 256
                    if pack_total_2 == pack_initial_total and pack_id == pack_initial_id:
                        frame_total = frame_total + data[32:]
                        #print("4")

                        if pack_num == pack_initial_total - 1:
                            self.cnt=self.cnt+1
                            #print("3")
                            #pack_initial_total = 0
                            #pack_initial_id = 0
                            #frame_total = b''
                            self.rawData.write(frame_total)
                            #self.container = av.open(self.rawData, format="h264", mode='r')
                            self.rawData.seek(self.cur_pos)
                            for packet in self.container.demux():
                                if packet.size == 0:
                                    continue
                                self.cur_pos += packet.size

                                for frame in packet.decode():
                                        #frame = packet.decode()
                                        bbb=frame.to_image()
                                        img = cv2.cvtColor(np.array(bbb), cv2.COLOR_RGBA2BGRA)
                                        image_message = marine_camera_node.bridge.cv2_to_imgmsg(img, encoding="passthrough")
                                        marine_camera_node.image_pub.publish(image_message)

                            pack_initial_total = 0
                            pack_initial_id = 0
                            frame_total = b''
            except Exception:
                print(Exception)


if __name__ == "__main__":
    rospy.init_node('marine_image_interface', anonymous=True)
    sudoPassword = '123'
    command = 'sudo route add -net 239.100.1.112 netmask 255.255.255.255 enp8s0'
    str = os.system('echo %s|sudo -S %s' % (sudoPassword, command))
    marine_camera_node=marine_camera_node()
    p1 = threading.Thread(target=marine_camera_node.read_data)
    p1.start()
    while 1:
        time.sleep(1)

