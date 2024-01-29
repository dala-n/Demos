import socket

### Assuming the server is already running ###

HOST = "127.0.0.1" # Standard loopback interface address on localhost
PORT = 65432 # Port to listen to (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # "with" context manager treats it as "file open", closes at the end of the with
    s.connect((HOST, PORT))
    s.sendall(b"Hello, World!")
    data = s.recv(1024)

print(f"Recieved {data!r}")