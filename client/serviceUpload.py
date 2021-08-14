import socket
import tqdm
import os
from pathlib import Path
import time

#/Users/abhisheknair/Desktop/Abhishek Nair Resume.pdf

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

class serviceUpload:
    def __init__(self, serverIP, port):
        self.serverIP = serverIP
        self.port     = port
        filename      = None
        filesize      = None
        s             = None

        self.getFileDir()
        self.openConnection()
        self.metaData()
        confVal = self.confirmationFromServer()
        if(confVal == "rec"):
            print("\033[92m[+] Server Ready to Recieve Data\033[0m")
            self.sendFile()
            print("\033[92m[+] File Sent Successfully\033[0m")
        else:
            print("\033[91mOOPS. Something Went Wrong\033[0m")
        
        self.closeConnection()
    
    
    def getFileDir(self):
        self.filename = input(f"Enter Directory:")
        self.filesize = os.path.getsize(self.filename)
    
    
    def openConnection(self):
        self.s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        print(f"\033[93m[+] Connecting to {self.serverIP}:{self.port}\033[0m")
        self.s.connect((self.serverIP, self.port))
        print("\033[92m[+] Connected to Server\033[0m")

    
    def metaData(self):
        code = "u"
        self.s.send(f"{self.filename}{SEPARATOR}{self.filesize}{SEPARATOR}{code}".encode())
        time.sleep(0.5)

    
    def confirmationFromServer(self):
        print("\033[93m[+] Waiting for Confirmation from Server...\033[0m")
        confirmationValue = self.s.recv(BUFFER_SIZE).decode()
        return confirmationValue
    

    def sendFile(self):
        print("\033[93m[+] Uploading File to Cloud...\033[0m")
        with open(f"{self.filename}", "rb") as f:
            while True:
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    break
                #encrypted = aes.encrypt(str(bytes_read), aes.password) # encrypt data
                #s.sendall(encrypted)
                self.s.sendall(bytes_read)

    
    def closeConnection(self):
        self.s.close()