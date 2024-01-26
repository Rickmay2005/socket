# Server 
import socket
import json

# Configurazione del server 
IP='127.0.0.1'
PORTA = 65432
DIM_BUFFER = 1024

#Creazione della socket del server con il costrutto with
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:

    sock_server.bind((IP,PORTA)) #assegno indirizzo IP  e porta al socket
    sock_server.listen() #server si mette in ascolto
    print("server in ascolto su {IP} {PORTA}")

    while True:
        #Ricevo i dati
        sock_service, addr = sock_server.accept()
        data = sock_service.recv(DIM_BUFFER).decode()
        data = json.loads(data)
        primoNumero = data['primoNumero']
        operazione = data['operazione']
        secondoNumero = data['secondoNumero']

        while True:
            #calcolo il risultato e lo invio
            risultato = 0
            if operazione == "+":
                risultato = primoNumero + secondoNumero
            elif operazione == "-":
                risultato = primoNumero - secondoNumero
            elif operazione == "*":
                risultato = primoNumero * secondoNumero
            elif operazione == "/":
                if secondoNumero != 0:
                    risultato = primoNumero / secondoNumero
                else:
                    risultato = "Impossibile"
            elif operazione == "%":
                risultato = primoNumero % secondoNumero


            sock_service.sendall(str(risultato).encode()) #Invia a tutti i client