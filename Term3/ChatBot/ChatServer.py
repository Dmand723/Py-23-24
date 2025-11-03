import threading
import socket
#Brodbent ip = 10.208.16.15
#IPv4 = 10.208.20.81
HOST = "26.119.56.160"
PORT = 1234 #0-65535
CLIENT_LIMIT = 1
activeClients = []

# hostName = socket.gethostname()
# IPAddr = socket.gethostbyname(hostName)
# print(IPAddr)


def clientHandler(client):
    '''handles the conection of client to the sever'''
    while True:
        userName = client.recv(2048).decode('utf-8')
        if userName != "":
            allWelcome = "Server~"+f"{userName} has joined the chat\n"
            if len(activeClients)> 0:
                sendMsgToAll(allWelcome)
            activeClients.append((userName,client))
            welcomeMsg = f"Server~Welcome to the server {userName} you can now send and recive messages"
            sendMsgToClient(client,welcomeMsg)
            print(userName, "Has connected")
            break
        else:
            print("no client username")
    threading.Thread(target=listenForMsg,args=(userName,client,)).start()

def listenForMsg(username,clinet):
    response = clinet.recv(2048).decode('utf-8')
    if response != '':
        finalMsg = str.format("{}~{}",username,response)
        sendMsgToAll(finalMsg)

def sendMsgToAll(msg):
    for user in activeClients:
        sendMsgToClient(user[1],msg)

def sendMsgToClient(client,msg):
    client.sendall(msg.encode())

def main():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        server.bind((HOST,PORT))
        print(f"server is Running at host {HOST} and port {PORT}")
    except:
        print(f"did not bind to the host {HOST} and port {PORT}")
    
    server.listen(CLIENT_LIMIT)
    while True:
       client, address = server.accept()
       print(f'Client has connected from {address[0]} {address[1]}')
       threading.Thread(target=clientHandler, args = (client,)).start()

if __name__ == '__main__':
    main()