import socket
import json
s = socket.socket(socket.AF_INET, socket. SOCK_DGRAM)
#Blocco 2

while True:
    #Ricevo i dati
    data, addr = s.recvfron(1024)
    if not data:
        break
data = data. decode()
data = json.loads(data)
primoNumero = data["primoNumero"]
operazione = data["operazione"]

secondoNumero = data["secondoNumero"]

#calcolo il risultato e lo invio
risultato = 0
if operazione == "+":
    risultato = primoNumero + secondoNumero
elif operazione == "-":
    risultato = primoNumero - secondoNumero
elif operazione == "+":
    risultato = primoNumero * secondoNumero
elif operazione == "/":
    if secondoNumero != 0:
        risultato = primoNumero / secondoNumero
    else:
        risultato = "Impossibile"
elif operazione == "%":
    risultato = primoNumero % secondoNumero

s.sendto(str(risultato).encode(), addr) #Invia a tutti i client