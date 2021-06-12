import os         #to get the path 
import socket     
import threading  #to seperate the clients

IP = socket.gethostbyname(socket.gethostname())  #assigning the host name dynamically using the socket.
PORT = 4456  # assigning a port number
ADDR = (IP, PORT) #creating a tuple with IP and PORT to get address 
SIZE = 1024 
FORMAT = "utf-8" 
SERVER_DATA_PATH = "server_data"

def handle_client(conn, addr):
    print(f"{addr} connected.")
    conn.send("OK@Welcome to the Server.".encode(FORMAT)) #cmd@message format is used.
    #@ is used to split the message and the cmd.


    #loop
    while True:
        data = conn.recv(SIZE).decode(FORMAT) #receive the cmd from the client
        data = data.split("@") 
        cmd = data[0]          

        if cmd == "UPLOAD":
            name, text = data[1], data[2]
            filepath = os.path.join(SERVER_DATA_PATH, name) 
            with open(filepath, "w") as f:
                f.write(text)

            send_data = "OK@File uploaded successfully."
            print("Received the file.")
            conn.send(send_data.encode(FORMAT))

        elif cmd == "EXIT":
            break

    print(f"Client {addr} disconnected")
    conn.close()

def main():
    print("Server is starting")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # using TCP server(Connection oriented), creating a server
    server.bind(ADDR) #binding the port and ip
    server.listen()   #server is listening
    print("Server is listening.")

    #creating a infinite loop 
    #waiting for cient to connect
    while True:
        conn, addr = server.accept() #server will accept the connection
        thread = threading.Thread(target=handle_client, args=(conn, addr)) #creating a seperate thread for each connection
        thread.start() 
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        

if __name__ == "__main__":
    main()