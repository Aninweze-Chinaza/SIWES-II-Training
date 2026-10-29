import socket

def startManagerServer():
    host = '127.0.0.1'
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
        serverSocket.bind((host, port))
        serverSocket.listen()
        print("Manager Terminal Active. Listening for cashier requests...")
        
        connection, address = serverSocket.accept()
        with connection:
            print(f"Cashier connected from {address}")
            
            while True:
                data = connection.recv(1024)
                if not data:
                    print("Cashier disconnected.")
                    break
                    
                rawMessage = data.decode('utf-8')
                
                # Protocol Enforcement
                if ":" in rawMessage:
                    msgType, content = rawMessage.split(":", 1)
                    validTypes = ["FUND", "TRANSFER", "CASHOUT"]
                    
                    if msgType.upper() in validTypes:
                        print(f"\n[{msgType.upper()}] Request: {content.strip()}")
                        response = f"Manager processed {msgType.upper()} request for: {content.strip()}"
                    else:
                        print(f"\n[UNKNOWN TAG] Raw text: {rawMessage}")
                        response = "Error: Unrecognized request type. Use FUND, TRANSFER, or CASHOUT."
                else:
                    print(f"\n[INVALID PROTOCOL] Raw text: {rawMessage}")
                    response = "Error: Invalid message format. Use TAG:Message."
                    
                connection.sendall(response.encode('utf-8'))

if __name__ == "__main__":
    startManagerServer()