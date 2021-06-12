import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4456
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024
def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create client
    client.connect(ADDR) #connecting the client

    #creating a infinite loop which will break when the exit command is used
    while True:
        data = client.recv(SIZE).decode(FORMAT) 
        cmd, msg = data.split("@") #spliting the cmd ad message

        if cmd == "OK":
            print(f"{msg}")

        data = input("> ")  #the input
        data = data.split(" ")  #split the data
        cmd = data[0] #the first message is the cmd


        if cmd == "EXIT":
            client.send(cmd.encode(FORMAT))
            break
        elif cmd == "UPLOAD":
            path = data[1]

            with open(f"{path}", "r") as f: #read the path
                text = f.read()

            filename = path.split("/")[-1] #get the file name
            send_data = f"{cmd}@{filename}@{text}" 
            client.send(send_data.encode(FORMAT)) #sending file to server

    print("Disconnected from the server.")
    client.close()

if __name__ == "__main__":
    main()
