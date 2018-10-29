# Abstract Summarization

**Prerequisite packages** -

1) [Python 3.6.6](https://www.python.org/downloads/release/python-366/)
2) [PyCharm 2018.2](https://download.jetbrains.com/python/pycharm-community-2018.2.3.exe)
    
    
**Install dependencies**

    python setup.py install
        
**Steps to download data**
1) Navigate to [CNN Mail](https://cs.nyu.edu/~kcho/DMQA/) - download 'stories' from CNN dataset.
2) Unzip the file.
3) Update the paths in config.py(inside POC project) as per you machine.
4) Navigate and download [fasttext vector](https://www.kaggle.com/yesbutwhatdoesitmean/wikinews300d1mvec) from kaggle.
5) create model folder (same place where we have data folder).
6) Unzip vector and put inside model folder.
7) Verify the paths in config.py.
    
**Steps to train model**

    1) Run data_preprocessing.py (make sure paths are corrected in config.py)
    2) Run train_model.py

**Prerequisite GPU support**    
1) Tensorflow currently support only NVIDIA GPUs (that to not all GPSus).
2) [Verify](https://www.addictivetips.com/windows-tips/check-dedicated-gpu/) if supported GPU is installed.
3) Check if GPU is [supported by CUDA](https://developer.nvidia.com/cuda-gpus). CUDA is required to integrate GPU and tensorflow.
4) Install latest version of [Cuda toolkit](https://en.wikipedia.org/wiki/CUDA) as per GPU* - download & install base and patch if exists.
5) Download and install [CUDNN](https://developer.nvidia.com/rdp/cudnn-download) as per Cuda version* (Need to register).
6) Known issues : [Step to install](https://medium.com/@kelfun5354/step-by-step-guide-to-install-tensorflow-cpu-gpu-for-windows-7-b472327984cd) and [VS integration issue](https://devtalk.nvidia.com/default/topic/1033111/cuda-setup-and-installation/cuda-9-1-cannot-install-due-to-failed-visual-studio-integration/2).

*Latest version of tensorflow required CUDA toolkit 9 and CUDNN 7.5.

**Enable GPU support**

    1) Make sure 'enable_gpu = True' in config.py
    2) From root of project run -
        python setup.py install 
       [Verify in logs that 'tensorflow-gpu==1.10.0' is installed]
    3) Run train_model.py

    
