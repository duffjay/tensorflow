# tensorflow
learning tensorflow and keras
## Environment
https://medium.com/@taylordenouden/installing-tensorflow-gpu-on-ubuntu-18-04-89a142325138

(XPS 8100) Ubuntu 16.04  
i7-860, no AVX instruction set support :(
TensorFlow assumes you have it - Anaconda may work?  (couldn't install TensorBoard?)  

(XPS 8930) - Ubuntu 18.04
GTX 1080 NVIDIA Driver 390  
CUDA 9.0 (Ubuntu 16.04)
cuDNN 7.0.5
- install runtime deb
- then install developer

### GPU Setup
https://gist.github.com/Mahedi-61/2a2f1579d4271717d421065168ce6a73
gcc 7.3  
NVIDIA Driver 390  
g++ 4:7.3.0  
freeglut3-dev  
build-essential  
libx11-dev  
libxmu-dev  
libxi-dev
libglu1-mesa  
libglu1-mesa-dev
gcc-6
g++-6
CUDA 9.0  https://developer.nvidia.com/cuda-90-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1704&target_type=runfilelocal  
STOPPED HERE (like, do this):  sudo ./cuda_9.0.176_384.81_linux.run
then install the patches (1,2,3,4)


### Python Setup
NOT using Anaconda.  Using virtualenv & virtualenvwrapper

### TensorFlow setup
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-tensorflow-on-ubuntu-16-04  

XPS 8100 (i7-860, GTX 1050) does not support AVX Instructions on the CPU - and aborts on import tensorflow; may need to build from source.  
XPS 8930 (i7-8700, GTX 1080) - Ubuntu 18.04 presents some extra challenges
CFA Dell Inspiron - (i7, GTX 1060m) Ubuntu 16.04

```
mkvirtualenv tgpu   # tgpu = tensorflow w/ gpu & CUDA
# you should have (tgpu) at the beginning of your prompt

# you only need to install once
pip install --upgrade tensorflow-gpu

# (after installing the first time)
# workon tgpu 
python3   # I'm on Python 3.5.2
>>> import tensorflow as tf

```

### Running this software
Clone to ~/projects  

You might have to adjust batch size  
Use this NVIDIA program to monitor GPU memory.  E.g. my GPU has 6 GB and there were memory allocation errors.  (decrease batch size)  
$ nvidia-smi  -l 1
