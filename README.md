# dependencies
ubuntu18.04
## pyav installation
1.pyav need ffmpeg > 4 ,if you use ```apt-get install ffmpeg to install ,default version will be ffmpeg 3.4 ,so you need to use instructions before to upgrade ffmpeg
```
sudo add-apt-repository ppa:jonathonf/ffmpeg-4
sudo apt upgrade
```
2.install dependencies of pyav
down load pyav source code from github
```
git clone https://github.com/PyAV-Org/PyAV.git

cd PyAV
source scripts/activate.sh

sudo apt-get install libmp3lame-dev libx264-dev libxvidcore-dev

pip install --upgrade -r tests/requirements.txt

./scripts/build-deps

# Build PyAV.
make

```
