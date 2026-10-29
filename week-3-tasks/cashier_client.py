import socket

def startCashierClient():
    host = '127.0.0.1'
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
        clientSocket.connect((host, port))
        print("Connected to Manager Terminal. Type 'quit' to exit.")
        print("Valid Protocol Tags: FUND, TRANSFER, CASHOUT")
        print("Format -> TAG:Details (e.g., CASHOUT:Ticket 9876 for N5000)")
        
        while True:
            message = input("\nEnter request: ")
            if message.lower() == 'quit':
                break
                
            clientSocket.sendall(message.encode('utf-8'))
            
            reply = clientSocket.recv(1024)
            print(f"Manager Reply: {reply.decode('utf-8')}")

if __name__ == "__main__":
    startCashierClient()