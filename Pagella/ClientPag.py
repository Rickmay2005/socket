#Client
import socket
import json

HOST = '127.0.0.1' #Dev'essere l'indirizzo IP del server
PORT = 22224 #Dev'essere la porta IP del server
DIM_BUFFER = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
    sock_service.connect((HOST, PORT))
    while True:
        primoNumero = float(input("Inserisci il primo numero: "))
        operazione = input("Inserisci l'operazione(simbolo)")
        secondoNumero = float(input("Inserisci il secondo numero: "))
        if(operazione==0):
            break
        dati = {"risposta":messaggio,
        "valori":risultato,
       }
        messaggio = json.dumps (messaggio)
        sock_service.sendall(messaggio.encode("UTF-8"))

        #Ricevo il risultato
        data = sock_service.recv(DIM_BUFFER)
        print("Risultato: ", data.decode())

        risposta=input("Continuare? S-N")
        if(risposta=="N"):
            break
    #socket chiusa automaticamente