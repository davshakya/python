import tkinter as tk
from tkinter import scrolledtext
import socket
import threading

# Client configuration
HOST = '127.0.0.1'
PORT = 55555

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat App")

        # Create a scrolled text widget to display the chat messages
        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
        self.chat_display.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        # Create an entry widget for typing messages
        self.message_entry = tk.Entry(root, width=30)
        self.message_entry.grid(row=1, column=0, padx=10, pady=10)

        # Create a button to send messages
        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

        # Client socket setup
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((HOST, PORT))

        # Receive messages in a separate thread
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()

    def send_message(self):
        # Get the message from the entry widget
        message = self.message_entry.get()

        # Send the message to the server
        self.client_socket.send(message.encode('utf-8'))

        # Display the message in the chat display
        self.display_message(f"You: {message}")

        # Clear the entry widget for the next message
        self.message_entry.delete(0, tk.END)

    def receive_messages(self):
        while True:
            try:
                # Receive message from the server
                message = self.client_socket.recv(1024).decode('utf-8')
                self.display_message(message)
            except ConnectionResetError:
                # Handle server disconnection
                self.display_message("Server disconnected.")
                break

    def display_message(self, message):
        # Insert a new message in the chat display
        self.chat_display.insert(tk.END, message + "\n")
        # Scroll to the bottom to show the latest message
        self.chat_display.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()
