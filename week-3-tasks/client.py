import socket

def startClient():
    # Must perfectly match the server's location
    serverHost = '127.0.0.1'
    serverPort = 65432

    # Step 1: Create the socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
        
        # Step 2: Connect to the server
        print(f"Attempting to connect to {serverHost}:{serverPort}...")
        clientSocket.connect((serverHost, serverPort))
        
        # Step 3: Send data
        message = "Ticket ID 4599, Stake 500"
        print(f"Sending message: {message}")
        # Encode string into raw bytes for network transit
        clientSocket.sendall(message.encode('utf-8'))
        
        # Step 4: Receive the response
        data = clientSocket.recv(1024)
        
    print(f"\n[SERVER REPLY]: {data.decode('utf-8')}")

if __name__ == "__main__":
    startClient()