'''
Created on Jan 26, 2016

@author: Ashwin
'''
import zipfile
from os.path import dirname
from nt import getcwd


with zipfile.ZipFile(dirname(getcwd())+'\\data\\0000021344_COCA COLA CO.zip','r') as z:
    z.extractall(dirname(getcwd())+'\\unzipped')