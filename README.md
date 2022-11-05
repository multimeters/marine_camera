# dependencies
ubuntu18.04
ros meolodic
## pyav installation
1.pyav need ffmpeg > 4 ,if you use ```apt-get install ffmpeg to install ,default version will be ffmpeg 3.4 ,so you need to use instructions before to upgrade ffmpeg
```
sudo add-apt-repository ppa:jonathonf/ffmpeg-4
sudo apt upgrade
```
2.download pyav source code from github
```
git clone https://github.com/PyAV-Org/PyAV.git
````
active virtual envirenment
```
cd PyAV
source scripts/activate.sh
```
install dependencie for ffmpeg4
```
sudo apt-get install libmp3lame-dev libx264-dev libxvidcore-dev
```
install dependencies for pillow
```
sudo apt-get install libjpeg-dev zlib1g-dev

sudo apt-get install libxml2-dev
```
install dependencies for pyav
```
pip install --upgrade -r tests/requirements.txt

./scripts/build-deps
```
make pyav
```
make
```
install py av
```
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple/ av

```
check pyav version
```
pyav --version
```
