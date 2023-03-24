import socket

# Der Header ist die Länge der Nachricht, die gesendet wird
HEADER = 64
# Der Port, auf dem der Server lauscht
PORT = 5050
# Die IP-Adresse des Servers (meine lokale IP-Adresse)
SERVER = "192.168.2.139"
# Die Adresse ist ein Tupel aus Server und Port
ADRESSE = (SERVER, PORT)
# Das Format ist UTF-8, in dem die Nachrichten kodiert werden
FORMAT = 'utf-8'
# Die Nachricht, die gesendet wird, wenn der Client die Verbindung trennt
DISCONNECT_MESSAGE = "bye"

# Der Client erstellt ein Socket-Objekt, das die Verbindung zum Server herstellt
# Das Socket-Objekt ist ein TCP-Socket
# TCP-Sockets sind bidirektionale Sockets, die eine Verbindung zwischen zwei Endpunkten herstellen
# TCP-Sockets sind zuverlässig, da sie die Übertragung von Daten überprüfen
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Der Client verbindet sich mit dem Server
client.connect(ADRESSE)

def send(msg):
    # Die Nachricht wird kodiert
    message = msg.encode(FORMAT)
    # Die Länge der Nachricht wird ermittelt
    msg_length = len(message)
    # Die Länge der Nachricht wird kodiert
    send_length = str(msg_length).encode(FORMAT)
    # Die Länge der Nachricht wird auf die Länge des Headers aufgefüllt
    send_length += b' ' * (HEADER - len(send_length))
    # Die Länge der Nachricht wird gesendet
    client.send(send_length)
    # Die Nachricht wird gesendet
    client.send(message)
    # Die Antwort des Servers wird empfangen und dekodiert
    print(client.recv(2048).decode(FORMAT))

# Der Client kann Nachrichten senden, bis er die Nachricht "bye" sendet
while True:
    msg = input("Enter a message: ")
    send(msg)
    if msg == DISCONNECT_MESSAGE:
        break
