# dependencies
ubuntu18.04

ros melodic

pyav

opencv

python3.6

net-tools

rospkg  ```pip3 install rospkg``` 

virtualenv  ```pip3 install virtualenv ```

pillow  ```pip3 install Pillow```

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

上面的指令如果报下面的错:
```
CFLAGS="-O0" LDFLAGS="" python3 setup.py build_ext --inplace --debug
Compiling av/logging.pyx because it changed.
[1/1] Cythonizing av/logging.pyx

Error compiling Cython file:
------------------------------------------------------------
...
cdef const char *log_context_name(void *ptr) nogil:
    cdef log_context *obj = <log_context*>ptr
    return obj.name

cdef lib.AVClass log_class
log_class.item_name = log_context_name
                      ^
------------------------------------------------------------

av/logging.pyx:216:22: Cannot assign type 'const char *(void *) except? NULL nogil' to 'const char *(*)(void *) noexcept nogil'. Exception values are incompatible. Suggest adding 'noexcept' to type 'const char *(void *) except? NULL nogil'.

Error compiling Cython file:
------------------------------------------------------------
...

# Start the magic!
# We allow the user to fully disable the logging system as it will not play
# nicely with subinterpreters due to FFmpeg-created threads.
if os.environ.get('PYAV_LOGGING') != 'off':
    lib.av_log_set_callback(log_callback)
```
这是由于cython升级造成的,需要卸载并安装Cython==0.29.21
```
cython --version
pip3 uninstall Cython
pip3 install Cython==0.29.21
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
