import socket

# Define the target host and port
target_host = "localhost"
target_port = 2301

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data (replace "Hello, UDP!" with your desired payload)
client_socket.sendto(b"Hello, UDP!", (target_host, target_port))

# Receive the response (optional)
response, addr = client_socket.recvfrom(4096)
print(f"Received response: {response.decode()}")

# Close the socket
client_socket.close()
