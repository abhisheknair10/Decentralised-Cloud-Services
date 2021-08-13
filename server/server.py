import socket
import tqdm
import os
from pathlib import Path
import time

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # receive 4096 bytes each time

class server:
    def __init__(self, IP, port):
        self.IP       = IP
        self.port     = port
        s             = None
        client_socket = None
        address       = None
        service       = None
        filename      = None
        filesize      = None
        recieved      = None

        self.openConnection()
        serviceVal = self.serviceRequest()
        if(self.serviceRequest == "10711"):
            self.s.send("10711".encode())
            self.recFile()
            if(self.filename == os.path.getsize(f"{home}/server_files/{self.filename}")):
                print("\033[92mFile Recieved Successfully \033[0m")
            else:
                print("\033[91mOOPS. Something Went Wrong\033[0m")
        else:
            print("\033[91mOOPS. Something Went Wrong\033[0m")
        
        self.closeConnection()

    
    def openConnection(self):
        self.s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        self.s.bind((self.IP, self.port))
        self.s.listen(5)
        print(f"[*] Listening as {self.IP}:{self.port}")
        self.client_socket, self.address = self.s.accept()
        self.address = self.address[0]
        print(f"\033[92m[+] {self.address} is connected\033[0m")
    

    def serviceRequest(self):
        self.recieved = self.client_socket.recv(BUFFER_SIZE).decode()
        self.filename, self.filesize, self.service = self.recieved.split(SEPARATOR)
        self.filename = os.path.basename(self.filename)
        self.filesize = int(self.filesize)
        return self.service

    
    def recFile(self):
        home = str(Path.home())
        with open(f"{home}/server_files/{self.filename}", "wb") as f:
            while True:
                bytes_read = self.client_socket.recv(BUFFER_SIZE)
                if not bytes_read:
                    time.sleep(0.5)
                    self.s.send(os.path.getsize(f"{home}/server_files/{self.filename}").encode())
                    break

                f.write(bytes_read)


    
    def closeConnection(self):
        self.client_socket.close()
        self.s.close()




serverActivity = server("::", 5001)