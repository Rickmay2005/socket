#Client
import socket
import json

HOST = '127.0.0.1' #Dev'essere l'indirizzo IP del server
PORT = 65432 #Dev'essere la porta IP del server


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service: #Con sock_service richiamo la funzione socket.socket... 
    sock_service.connect((HOST, PORT))
    while True:
        primoNumero = float(input("Inserisci il primo numero: "))
        operazione = input("Inserisci l'operazione(simbolo)")
        secondoNumero = float(input("Inserisci il secondo numero: "))
        if(operazione==0):
            break
        messaggio = {'primoNumero' : primoNumero,
                    'operazione' : operazione,
                    'secondoNumero' : secondoNumero}
        messaggio = json.dumps (messaggio)

        sock_service.sendall(messaggio.encode("UTF-8"))

        #Ricevo il risultato
        data = sock_service.recv(1024)
        print("Risultato: ",  data.decode())

          