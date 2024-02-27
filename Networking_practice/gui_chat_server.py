import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 55555

# List to store connected clients
clients = []

# Server socket setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

def handle_client(client_socket, addr):
    while True:
        try:
            # Receive message from the client
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break

            # Broadcast the message to all clients
            broadcast(f'{addr[0]}:{addr[1]}: {message}', client_socket)

        except ConnectionResetError:
            # Remove disconnected client
            clients.remove(client_socket)
            break

def broadcast(message, sender_socket):
    for client in clients:
        # Send message to all clients except the sender
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except socket.error:
                # Remove disconnected client
                clients.remove(client)

# Accept and handle incoming connections
print(f"Server listening on {HOST}:{PORT}")

while True:
    client_socket, addr = server_socket.accept()
    clients.append(client_socket)

    # Create a thread to handle the new client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_thread.start()
