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

if(service == "u"):
    uploadToCloud = serviceUpload.serviceUpload("2001:8f8:1329:8bd6:4885:1b08:ced8:9a25", 5001)

