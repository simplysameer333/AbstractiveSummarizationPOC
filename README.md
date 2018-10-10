**Abstract Summarization** 

**Prerequisite packages** -

    1) Python 3.6.6 - https://www.python.org/downloads/release/python-366/
    2) PyCharm 2018.2 - https://download.jetbrains.com/python/pycharm-community-2018.2.3.exe
    
**Install dependencies**

    python setup.py install
        
**Steps to download data**

    1) Navigate to https://cs.nyu.edu/~kcho/DMQA/ - download 'stories' from CNN dataset
    2) Unzip the file.
    3) Update the paths in config.py as per you machine.
    4) Navigate to https://www.kaggle.com/yesbutwhatdoesitmean/wikinews300d1mvec and download
    5) create model folder (same place where we have data folder)
    6) Unzip vector and put inside model folder.
    7) Verify the paths in config.py
    
**Steps to train model**

    1) Run data_preprocessing.py (make sure paths are corrected in config.py)
    2) Run train_model.py
