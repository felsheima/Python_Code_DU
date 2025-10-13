#Very Simple Honeypot project creation
#Allison Felsheim

import socket
import logging
import datetime

#Configure logging
logging.basicConfig(filename='honeypot.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def honeypot(host='0.0.0.0', port=80):
    #1. Create a socket object 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #2. Bind the socket to the host and port
    server_socket.bind((host, port))

    #3. Listen for incoming connections
    server_socket.listen(10)
    print(f'\nHoneypot is running on {host}:{port}')

    #4. Accept a connection
    while True:
        print(f'\nWaiting for a connection......')
        client_socket, client_address = server_socket.accept()

        print(f'\nConnected by {client_address} ')

        #5. Recieve and send data
        logging.info(f'Connection from {client_address} ')
        #Since you're working with network sockets, you have to send and recieve data by bytes....which is what the b does
        client_socket.send(b"Hello, you've reached a honeypot!\n")

        #6. CLose the connection
        client_socket.close()

if __name__ =="__main__":
    honeypot()
