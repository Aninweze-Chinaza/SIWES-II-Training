import socket

def startServer():
    # '127.0.0.1' is the standard loopback IP address (localhost). 
    # It means the server is running on this exact laptop.
    serverHost = '127.0.0.1' 
    serverPort = 65432       # Port to listen on (non-privileged ports are > 1023)

    # Step 1: Create the socket (AF_INET = IPv4, SOCK_STREAM = TCP)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
        
        # Step 2: Bind the socket to the specific IP and Port
        serverSocket.bind((serverHost, serverPort))
        
        # Step 3: Listen for incoming connections
        serverSocket.listen()
        print(f"Server is listening on {serverHost}:{serverPort}...")
        print("Waiting for a client to connect...")
        
        # Step 4: Accept the connection when a client knocks
        # This code pauses here and waits until someone actually connects
        connection, clientAddress = serverSocket.accept()
        
        with connection:
            print(f"\n[SUCCESS] Connected by client at {clientAddress}")
            
            while True:
                # Step 5: Receive the data (1024 bytes at a time)
                data = connection.recv(1024)
                if not data:
                    break
                
                # Decode the raw bytes back into a readable string
                clientMessage = data.decode('utf-8')
                print(f"Client says: {clientMessage}")
                
                # Step 6: Send a response back
                response = f"Server received your message: '{clientMessage}'"
                connection.sendall(response.encode('utf-8'))

if __name__ == "__main__":
    startServer()