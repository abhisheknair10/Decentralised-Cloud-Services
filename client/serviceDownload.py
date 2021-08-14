import socket
import tqdm
import os
from pathlib import Path
import time


SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

class serviceDownload:
    def __init__(self, serverIP, port):
        self.serverIP = serverIP
        self.port     = port
        s             = None
        filename      = None
        filesize      = None
        home          = None


        self.filename = input("Enter File name to Retrieve: ")
        print(self.filename)
        self.openConnection()
        self.metaData()
        self.recFile()
        print("\033[92mFile Downloaded from Cloud Successfully\033[0m")
        self.closeConnection()
        

    def openConnection(self):
        self.s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        print(f"\033[93m[+] Connecting to {self.serverIP}:{self.port}\033[0m")
        self.s.connect((self.serverIP, self.port))
        print("\033[92m[+] Connected to Server\033[0m")

    
    def metaData(self):
        code = "d"
        self.filesize = 0
        self.s.send(f"{self.filename}{SEPARATOR}{self.filesize}{SEPARATOR}{code}".encode())
        time.sleep(0.5)

    
    def recFile(self):
        print("\033[93m[+] Recieiving File Contents...\033[0m")
        self.home = str(Path.home())
        with open(f"{self.home}/downloads/{self.filename}", "wb") as f:
            while True:
                bytes_read = self.s.recv(BUFFER_SIZE)
                if not bytes_read:
                    break

                f.write(bytes_read)


    def closeConnection(self):
        self.s.close()