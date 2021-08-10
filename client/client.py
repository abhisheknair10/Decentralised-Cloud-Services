import socket
import tqdm
import os
from pathlib import Path
#import aes

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

class serverComm:
    serverIP = "2001:8f8:1329:8bd6:395a:7165:671e:3a13"
    port = 5001
    filename = None
    filesize = None
    s = None

    def __init__(self):
        self.getFileDir()
        self.openConnection(serverComm.serverIP, serverComm.port)
        self.fileMetaData()
        self.sendFile()
        serverComm.s.close()


    def getFileDir(self):
        serverComm.filename = "testFile.txt"
        serverComm.filesize = os.path.getsize(serverComm.filename)


    def openConnection(self, serverIP, port):
        serverComm.s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        print(f"[+] Connecting to {serverComm.serverIP}:{port}")
        serverComm.s.connect((serverComm.serverIP, port))
        print("[+] Connected.")


    def fileMetaData(self):
        serverComm.s.send(f"{serverComm.filename}{SEPARATOR}{serverComm.filesize}".encode())


    def sendFile(self):
        progress = tqdm.tqdm(range(serverComm.filesize), f"Sending {serverComm.filename}", unit="B", unit_scale=True, unit_divisor=1024)

        with open(f"{serverComm.filename}", "rb") as f:
            while True:
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    break

                #encrypted = aes.encrypt(str(bytes_read), aes.password) # encrypt data
                #s.sendall(encrypted)
                serverComm.s.sendall(bytes_read)

                progress.update(len(bytes_read))


uploadToCloud = serverComm()
del uploadToCloud
