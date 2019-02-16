# tensorflow
learning tensorflow and keras
## Environment
https://medium.com/@taylordenouden/installing-tensorflow-gpu-on-ubuntu-18-04-89a142325138

Ubuntu 16.04  
GTX 1080 NVIDIA Driver 390  
CUDA 9.0 (Ubuntu 16.04)
cuDNN 7.0.5
- install runtime deb
- then instell developer

### setup
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-tensorflow-on-ubuntu-16-04  

XPS 8100 does not support AVX Instructions on the CPU - and aborts on import tensorflow; may need to build from source.  
XPS 8930 - Ubuntu 18.04 presents some extra challenges

```
mkdir ~/tf-demo
cd ~/tf-demo
python3 -m venv tensorflow-dev
pip3 install --upgrade tensorflow-gpu
python #(3.5.2)
>>> import tensorflow as tf

```

### resume
```
cd ~/tf-demo
source tensorflow-dev/bin/activate
python3
```
