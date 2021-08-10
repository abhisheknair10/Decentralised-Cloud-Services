import socket
import tqdm
import os
from pathlib import Path
import time

#import aes

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

class connectToServer:
    def __init__(self, serverIP, port):
        self.serverIP = serverIP
        self.port     = port
        filename      = None
        filesize      = None
        s             = None


    def getFileDir(self):
        self.filename = "testFile.txt"
        self.filesize = os.path.getsize(self.filename)


    def openConnection(self, serverIP, port):
        self.s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        print(f"[+] Connecting to {self.serverIP}:{self.port}")
        self.s.connect((self.serverIP, self.port))
        print("[+] Connected.")


    def fileMetaData(self):
        self.s.send(f"{self.filename}{SEPARATOR}{self.filesize}".encode())


    def sendFile(self):
        with open(f"{self.filename}", "rb") as f:
            while True:
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    print("\033[92mFile Sent Successfully \033[0m")
                    break

                #encrypted = aes.encrypt(str(bytes_read), aes.password) # encrypt data
                #s.sendall(encrypted)
                self.s.sendall(bytes_read)
    
    def closeConnection(self):
        self.s.close()


uploadToCloud = connectToServer("2001:8f8:1329:8bd6:395a:7165:671e:3a13", 5001)
uploadToCloud.getFileDir()
uploadToCloud.openConnection(uploadToCloud.serverIP, uploadToCloud.port)
uploadToCloud.fileMetaData()
uploadToCloud.sendFile()
uploadToCloud.closeConnection()

del uploadToCloud
