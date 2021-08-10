import socket
import tqdm
import os
from pathlib import Path

# device's IP address
SERVER_HOST = "::"
SERVER_PORT = 5001

BUFFER_SIZE = 4096 # receive 4096 bytes each time
SEPARATOR = "<SEPARATOR>"

# create the server socket
s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

# bind the socket to our local address
s.bind((SERVER_HOST, SERVER_PORT))

# enabling our server to accept connections
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

client_socket, address = s.accept()
address = address[0]

print(f"[+] {address} is connected.")

# receive the file infos
received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR)

# remove absolute path if there is
filename = os.path.basename(filename)
# convert to integer
filesize = int(filesize)

# start receiving the file from the socket
progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)

home = str(Path.home())
with open(f"{home}/Downloads/{filename}", "wb") as f:
   while True:
       bytes_read = client_socket.recv(BUFFER_SIZE)
       if not bytes_read:
           break
       
       f.write(bytes_read)
       
       progress.update(len(bytes_read))

# close the client socket
client_socket.close()
# close the server socket
s.close()