#!/usr/bin/env python3
import struct
import time
import socket
import av
import cv2
import io
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import sys
import rospy
#
class image_converter:

  def __init__(self):
    self.image_pub = rospy.Publisher("image_topic_2",Image)
    self.container = av.open("/home/lhl/lq_mapfusion/lq/src/marine_camera/nodes/test2.H264",format="h264")
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("image_topic",Image,self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

    (rows,cols,channels) = cv_image.shape
    if cols > 60 and rows > 60 :
      cv2.circle(cv_image, (50,50), 10, 255)

    cv2.imshow("Image window", cv_image)
    cv2.waitKey(3)

    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
    except CvBridgeError as e:
      print(e)
def receiver():       
          for packet in image_converter.container.demux():
          # Do something with `packet`, often:                       
              for frame in packet.decode():
                  # Do something with `frame`.
                  # self.frames.append(frame)
                  # ����ȡ����֡���б���
                  print("process frame: %04d (width: %d, height: %d)" % (
                  frame.index, frame.width, frame.height))
                  #frame.VideoFrame.to_image().save('frame-%04d.jpg' % frame.index)
                  nnn=frame.to_ndarray()
                  bbb=frame.to_image()
                  #plt.imshow(bbb)
                  #plt.show()
                  print(nnn.size)
                  #cv.waitKey(0)
                  img = cv2.cvtColor(np.array(bbb), cv2.COLOR_RGBA2BGRA)
                  image_message = image_converter.bridge.cv2_to_imgmsg(img, encoding="passthrough")
                  image_converter.image_pub.publish(image_message)
                  #cv2.imshow("test", img)
                  #cv2.waitKey(0)
                  #cv2.destroyAllWindows()
                  #frame.to_image()
                  # ת����ͼ�񣬲����ñ���·��
                  #frame1 = VideoFrame(1920, 1080, 'rgb24')
                  #cc=frame.to_image()#.save("test%04d.jpg" % frame.index)
                  #frame.to_image().save("frame.jpg")
                  # �������������½��г�ʼ�����Ա�����һ֡���д洢
                  pack_initial_total = 0
                  pack_initial_id = 0

if __name__ == "__main__":
    rospy.init_node('image_converter', anonymous=True)
    image_converter=image_converter()
    #receiver()
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        for packet in image_converter.container.demux():
          # Do something with `packet`, often:                       
              for frame in packet.decode():
                  # Do something with `frame`.
                  # self.frames.append(frame)
                  # ����ȡ����֡���б���
                  print("process frame: %04d (width: %d, height: %d)" % (
                  frame.index, frame.width, frame.height))
                  #frame.VideoFrame.to_image().save('frame-%04d.jpg' % frame.index)
                  nnn=frame.to_ndarray()
                  bbb=frame.to_image()
                  #plt.imshow(bbb)
                  #plt.show()
                  print(nnn.size)
                  #cv.waitKey(0)
                  img = cv2.cvtColor(np.array(bbb), cv2.COLOR_RGBA2BGRA)
                  image_message = image_converter.bridge.cv2_to_imgmsg(img, encoding="passthrough")
                  image_converter.image_pub.publish(image_message)
                  #cv2.imshow("test", img)
                  #cv2.waitKey(0)
                  #cv2.destroyAllWindows()
                  #frame.to_image()
                  # ת����ͼ�񣬲����ñ���·��
                  #frame1 = VideoFrame(1920, 1080, 'rgb24')
                  #cc=frame.to_image()#.save("test%04d.jpg" % frame.index)
                  #frame.to_image().save("frame.jpg")
                  # �������������½��г�ʼ�����Ա�����һ֡���д洢
                  pack_initial_total = 0
                  pack_initial_id = 0
        image_converter.container = av.open("/home/lhl/lq_mapfusion/lq/src/marine_camera/nodes/test2.H264",format="h264")
    rate.sleep()
