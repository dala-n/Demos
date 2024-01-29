import socket

HOST = "127.0.0.1" # Standard loopback interface address on localhost
PORT = 65432 # Port to listen to (non-privileged ports are > 1023)

# socket.AF_INET is iPV4
# socket.SOCK_STREAM is tcp
# sock.SOCK_DGRAM (datagram) is udp

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # "with" context manager treats it as "file open", closes at the end of the with
    s.bind((HOST, PORT)) # assigns/binds local host to an ip address and a port number (65432)
    s.listen() # Server calls listen, waiting for a connection
    conn, addr = s.accept() # When the echo client connects, it accepts the connection. 'conn' is a 'connection' separate socket in order to be able to listen for more connections
    with conn:
        print(f"connected by {addr}") # print out the address, port assigned
        while True: # infinite loop
            data = conn.recv(1024)
            if not data: # if data is empty
                break # breaks the connection
            conn.sendall(data) # otherwise send the data back
# once nothing is left, it terminates