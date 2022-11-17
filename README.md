# dependencies
ubuntu18.04

ros melodic

pyav

opencv

python3.6

net-tools

rospkg  ```pip3 install rospkg``` 

virtualenv

## pyav installation
pyav not surpport python2. use pip to install ptav will fail . use pip3 instead 

1.pyav need ffmpeg > 4 ,if you use apt-get install ffmpeg to install ,default version will be ffmpeg 3.4 ,so you need to use instructions before to upgrade ffmpeg
```
sudo add-apt-repository ppa:jonathonf/ffmpeg-4
sudo apt upgrade
```
2.download pyav source code from github
```
git clone https://github.com/PyAV-Org/PyAV.git
````
3.active virtual envirenment
```
cd PyAV
source scripts/activate.sh
```
4.install dependencie for ffmpeg4
```
sudo apt-get install libmp3lame-dev libx264-dev libxvidcore-dev
```
5.install dependencies for pillow
```
sudo apt-get install libjpeg-dev zlib1g-dev

sudo apt-get install libxml2-dev
```
6.install dependencies for pyav
```
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple/ --upgrade -r tests/requirements.txt

./scripts/build-deps
```
7.make pyav
```
make
```
8.install py av
```
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple/ av

```
9.check pyav version
```
pyav --version
```
## opencv-python installation
```
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple scikit-build

sudo apt-get install cmake

pip3 install --upgrade pip -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

pip3 install opencv-python -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com



```
