from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time
from person import Person

# GLOBAL CONSTANTS
HOST = 'localhost'
PORT = 5500
BUFSIZ = 1024
ADDR = (HOST, PORT)
MAX_CONNECTIONS = 10
BUFSIZ = 512

# GLOBAL VARIABLES
clients = []

def broadcast():


def client_communication(person):
    """
    Thread to handle all messages from client
    :param client: Person
    :return: None
    """
    client = person.client

    # get persons name
    name = client.recv(BUFSIZ).decode("utf8")
    msg = f"{name} has joined the chat!"
    broadcast(msg) # broadcast welcome message

    while True:
        msg = client.recv(BUFSIZ)
        if msg == bytes("{quit}", "utf8"):
            broadcast(f"{name} has left the chat...", "")
            client.send(bytes("{quit}", "utf8"))
            client.close()
            persons.remove(person)
        else:
            broadcast(msg, name)


def wait_for_connection():
    """
    Wait for connection from new client, start new thread once connected
    :param SERVER: SOCKET
    :return: None
    """
    run = True
    while run:
        try:
            client, addr = SERVER.accept()
            Thread(target=client_communication, args=(client,)).start()
        except Exception as e:
            print("[FAILURE]", e)
            run = False

    print("SERVER CRASHED")

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(MAX_CONNECTIONS) # listen for connections
    print("[STARTED] Waiting for connections...")
    ACCEPT_THREAD = Thread(target=wait_for_connection)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()

