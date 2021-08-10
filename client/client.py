import socket
import tqdm
import os
import aes

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

# the ip address or hostname of the server, the receiver
host = "2001:8f8:1329:8bd6:2d74:8b37:c3e3:8796"
port = 5001

filename = "Abhishek Nair - Resume.pdf"
filesize = os.path.getsize(filename) # get the file size

# create the client socket
s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")

# send the filename and filesize
s.send(f"{filename}{SEPARATOR}{filesize}".encode())

# send the file
progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)

with open(filename, "rb") as f:
    while True:
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            break
        
        #encrypted = aes.encrypt(str(bytes_read), aes.password) # encrypt data
        #s.sendall(encrypted)
        s.sendall(bytes_read)
        
        progress.update(len(bytes_read))

s.close()