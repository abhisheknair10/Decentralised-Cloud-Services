import socket
import tqdm
import os
from pathlib import Path
import time

import serviceUpload
#import aes


CURRENT_DIR = os.getcwd()
os.chdir("/")

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

print("For Uploading File to Cloud, Enter 'u'")
print("For Downloading File from  Cloud, Enter 'd'")
service = input("Enter Service: ")

ip = "2001:8f8:1329:8bd6:5db8:b877:7d08:4a61"
port = 5001

if(service == "u"):
    uploadToCloud = serviceUpload.serviceUpload(ip, port)
elif(service == "d"):
    downloadFromCloud = serviceDownload.serviceDownload(ip, port)