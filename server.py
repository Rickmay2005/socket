import socket

SERVER_IP="127.0.0.1"
SERVER_PORT=5005
BUFFER_SIZE=1024

#creo socket
sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP,SERVER_PORT))

print("Server in attesa del messaggio")

while True:
    #Ricezione
    data,addr=sock.recvfrom(BUFFER_SIZE)
    print(f"Messaggio ricevuto dal client {addr}:{data.decode()}")

    #invio risposta al client
    reply="pong"
    sock.sendto(reply.encode(), addr)