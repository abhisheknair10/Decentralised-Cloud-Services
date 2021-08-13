import socket
import tqdm
import os
from pathlib import Path
import time

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
        if(confVal == "7975"):
            self.sendFile()
            filesizeVal = self.checkFileSizeRecieved()
            if(filesizeVal == self.filesize):
                print("\033[92mFile Sent Successfully\033[0m")
            else:
                print("\033[91mOOPS. Something Went wrong when Uploading the File\033[0m")
        else:
            print("\033[91mOOPS. Something Went Wrong\033[0m")
        
        self.s.closeConnection()
    
    
    def getFileDir(self):
        self.filename = input(f"Enter Directory:")
        self.filesize = os.path.getsize(self.filename)
    
    
    def openConnection(self):
        self.s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        print(f"[+] Connecting to {self.serverIP}:{self.port}")
        self.s.connect((self.serverIP, self.port))
        print("\033[92m[+] Connected to Server\033[0m")

    
    def metaData(self):
        self.s.send(f"{self.filename}{SEPARATOR}{self.filesize}{SEPARATOR}10711".encode())
        time.sleep(0.5)

    
    def confirmationFromServer(self):
        print("[+] Waiting for Confirmation from Server...")
        confirmationValue = self.s.accept()
        confirmationValue = confirmationValue.recv(BUFFER_SIZE).decode().split(SEPARATOR)
        return confirmationValue
    

    def sendFile(self):
        with open(f"{self.filename}", "rb") as f:
            while True:
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    break

                #encrypted = aes.encrypt(str(bytes_read), aes.password) # encrypt data
                #s.sendall(encrypted)
                self.s.sendall(bytes_read)


    def checkFileSizeRecieved(self):
        print("[+] Confirming Upload to Server...")
        filesizeVal = self.s.accept()
        filesizeVal = filesizeVal.recv(BUFFER_SIZE).decode().split(SEPARATOR)
        return filesizeVal

    
    def closeConnection(self):
        self.s.close()