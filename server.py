import socket 
import threading
import time
import sys

# Der Header ist die Länge der Nachricht
HEADER = 64
# Der Port, auf dem der Server lauscht
PORT = 5050
# Der Server ist die IP-Adresse des Servers
SERVER = socket.gethostbyname(socket.gethostname())
# Die Adresse ist die Kombination aus Server und Port
ADRESSE = (SERVER, PORT)
# Der Format ist der Format, in welchem die Nachrichten codiert werden
FORMAT = 'utf-8'
# Die Disconnect Message ist die Nachricht, die der Client an den Server sendet, wenn er sich abmelden möchte
DISCONNECT_MESSAGE = "bye"

# Der Server wird erstellt
# socket.AF_INET ist die Adresse des Servers
# socket.SOCK_STREAM ist die Protokollart (TCP in diesem Fall)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Der Server wird an die Adresse gebunden
server.bind(ADRESSE)

def handle_client(conn, adr):
    print(f"Der Client mit der Adresse {adr} hat sich verbunden")
    connected = True

    while connected:
        # Die Nachricht wird empfangen
        msg_length = conn.recv(HEADER).decode(FORMAT)
        # Wenn die Nachricht nicht leer ist, wird sie ausgegeben
        if msg_length:
            msg_length = int(msg_length)
            # Die Nachricht wird empfangen
            msg = conn.recv(msg_length).decode(FORMAT)
            # Wenn die Nachricht DISCONNECT_MESSAGE ist, wird connected auf False gesetzt
            # überprüfe ob DISCONNECT_MESSAGE gleich msg ist
            print(msg)
            # Die Nachricht wird ausgegeben
            print(f"[{adr}] {msg}")
            # Die Client wird über die Ankunft der Nachricht informiert
            if msg == DISCONNECT_MESSAGE:
                conn.send("Der Client hat sich abgemeldet".encode(FORMAT))
                connected = False
                sys.exit()
            if msg in ["game", "Game", "GAME"]:
                game()
            conn.send("Msg received".encode(FORMAT))

def game():
    print("Schere Steins Papier startet jetzt!")
     
        
def start():
    # Der Server hört auf eingehende Verbindungen
    server.listen()
    print(f"Server läuft auf der IP Adresse {SERVER}")
    while True:
        # Der Server akzeptiert eingehende Verbindungen
        conn, addr = server.accept()
        # Der Thread wird gestartet
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        # Die Anzahl der aktiven Verbindungen wird ausgegeben
        print(f"Es sind aktuell {threading.activeCount() - 1} Verbindungen aktiv")

# write a method where you can send a message to the client from the server


print("Beep Boop, der Server läuft")
start()
