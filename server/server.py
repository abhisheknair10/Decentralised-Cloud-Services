import socket
import tqdm
import os
from pathlib import Path

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # receive 4096 bytes each time

class connectToClient:
    def __init__(self, IP, port):
        self.IP       = IP
        self.port     = port
        s             = None
        client_socket = None
        address       = None
        filename      = None
        filesize      = None
        recieved      = None


    def openConnection(self):
        self.s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        self.s.bind((self.IP, self.port))
        self.s.listen(5)
        print(f"[*] Listening as {self.IP}:{self.port}")
        self.client_socket, self.address = self.s.accept()
        self.address = self.address[0]
        print(f"[+] {self.address} is connected")


    def fileMetaData(self):
        self.recieved = self.client_socket.recv(BUFFER_SIZE).decode()
        self.filename, self.filesize = self.recieved.split(SEPARATOR)
        self.filename = os.path.basename(self.filename)
        self.filesize = int(self.filesize)


    def recFile(self):
        home = str(Path.home())
        with open(f"{home}/Downloads/{self.filename}", "wb") as f:
           while True:
               bytes_read = self.client_socket.recv(BUFFER_SIZE)
               if not bytes_read:
                   print("\033[92mFile Recieved Successfully \033[0m")
                   break

               f.write(bytes_read)


    def closeConnection(self):
        self.client_socket.close()
        self.s.close()


recieve = connectToClient("::", 5001)
recieve.openConnection()
recieve.fileMetaData()
recieve.recFile()
recieve.closeConnection()

del recieve
