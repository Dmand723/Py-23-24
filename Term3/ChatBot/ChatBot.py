import threading
import socket
import tkinter as tk
from tkinter import *
from tkinter import Misc
from tkinter import messagebox
from tkinter import scrolledtext
#TEHE ip 10.208.20.135
#jax ip N/A


class ChatApp(Frame):
    HOST = "26.119.56.160"
    PORT = 1234 #0-65535

    Nyanza = "#DFF2D8"
    TeaGreen = "#C6DEA6"
    Verdigris = "#7EBDC3"
    Wenge = "#7A6263"
    Sage = "#CED097"

    Lavender = "#D8D4F2"
    Thistle = "#C4B2BC"
    DarkThistle = "#968790"
    Beaver = "#A29587"
    Coyote = "#846C5B"
    RaisinBlack = "#332E3C"

    Font = ("Comic Sans MS",17)
    SMALL_FONT = ("Great Vibes",13)
    BUTTON_FONT =("Great Vibes",15)
    def __init__(self,root):
        super().__init__(root)
        self.root = root
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.rootSetup()
        self.createWidgets()
    
    def createWidgets(self):
        """Creates All Widgets For ChatBot App"""
        self.createFrames()
        
        

    def rootSetup(self):
        """Setup for root settings"""
        self.root.geometry("770x720")
        self.root.title("Chat App")
        self.root.resizable(False,False)

        self.root.grid_rowconfigure(0,weight=1)
        self.root.grid_rowconfigure(1,weight=4)
        self.root.grid_rowconfigure(2,weight=1)

        

    def createFrames(self):
        '''Create and Setup Frames on App'''
        self.topFrame = Frame(self.root,width=600,height=100,bg=ChatApp.RaisinBlack,highlightbackground=ChatApp.Nyanza,highlightthickness=1)
        self.middleFrame = Frame(self.root,width=600,height=400,bg=ChatApp.Thistle,highlightbackground=ChatApp.Nyanza,highlightthickness=1)
        self.bottomFrame = Frame(self.root,width=600,height=100,bg=ChatApp.RaisinBlack,highlightbackground=ChatApp.Nyanza,highlightthickness=1)

        self.topFrame.grid(row=0,column=0,sticky=NSEW)
        self.middleFrame.grid(row=1,column=0,sticky=NSEW)
        self.bottomFrame.grid(row=2,column=0,sticky=NSEW)

        #Setup top frame
        self.userNameLbl = Label(self.topFrame,text="Enter Username",font=ChatApp.Font,bg=ChatApp.RaisinBlack,fg=ChatApp.Lavender)
        self.userNameLbl.pack(side=LEFT,padx=10,pady=5)
        
        self.userNameTxb = Entry(self.topFrame,font=ChatApp.Font,bg=ChatApp.Coyote,fg=ChatApp.Lavender,width=20)
        self.userNameTxb.pack(side=LEFT,padx=15,pady=5)

        self.joinBtn = Button(self.topFrame,font=ChatApp.BUTTON_FONT,text="Join",bg=ChatApp.Thistle,fg=ChatApp.Lavender,width=9,command=self.connect)
        self.joinBtn.pack(side=LEFT,padx=5,pady=5)

        #Setup Middle Frame
        self.msgWindow = scrolledtext.ScrolledText(self.middleFrame, font=ChatApp.SMALL_FONT,
                                                    bg=ChatApp.DarkThistle,
                                                    fg=ChatApp.Lavender,
                                                    width=60,
                                                    height=26.5,wrap=WORD)
        self.msgWindow.config(state=tk.DISABLED)
        self.msgWindow.pack(side=TOP, padx=10, pady=10)

        #Setup Bottom Frame
        self.msgTxb = Entry(self.bottomFrame,font=ChatApp.Font,bg=ChatApp.Coyote,fg=ChatApp.Lavender,width=20)
        self.msgTxb.pack(side=LEFT,padx=15,pady=5)

        self.msgBtn = Button(self.bottomFrame,font=ChatApp.BUTTON_FONT,text="Send",bg=ChatApp.Thistle,fg=ChatApp.Lavender,width=9,command=self.sendMsg)
        self.msgBtn.pack(side=LEFT,padx=5,pady=5)

    def sendMsg(self):
            msg = self.msgTxb.get()
            if msg != "":
                self.client.sendall(msg.encode())
                self.msgTxb.delete(0,len(msg))
            else:
                messagebox.showerror("Error","Empty Message")
                exit(0)


    def connect(self):
        userName = self.userNameTxb.get()
        if userName != "":
            self.client.sendall(userName.encode())
        else:
            print("Username can not be empty")
            exit(0)
        threading.Thread(target=self.listenForServerMsg,args=(self.client,)).start()
        self.setState(self.userNameTxb,"disabled")
        self.joinBtn.config(text="Leave",command=self.leaveServer)
        self.sendMsgToServer(self.client)
        try:
            self.client.connect((ChatApp.HOST,ChatApp.PORT)) 
            messagebox.showinfo("Connected","Connected to server")    
        except:
            messagebox.showerror("Error"f'did not connect to server host {ChatApp.HOST} and port {ChatApp.PORT}')
            exit(0)
 

    def setState(self,object,state = str):
        """Sets the state to object to disabled or normal"""

    def leaveServer(self):
        msg = "Server: "+self.userNameTxb.get() + "has left"
        self.client.sendall(msg.encode())
        self.client.shutdown(2)
        exit(0)

    def updateMsgWindow(self,msg):
        self.msgWindow.config(state=NORMAL)
        self.msgWindow.insert(END,msg+"\n")
        self.msgWindow(state=DISABLED)

    def listenForServerMsg(self,client):
        """Allowing you yo receve messages from thr server"""
        while True:
            msg = client.recv(2048).decode("utf-8")
            if msg != "":
                username = msg.split("~")[0]
                content = msg.split("~")[1]
                if username.upper() == "SERVER":
                    self.updateMsgWindow(f"{username}:"+  f"{content}")
                else:
                    print(f"{username}:"+ f"{content}")
            else:
                print("No Msg")











def main():
    root = Tk()
    app = ChatApp(root)
    root.mainloop()
    
    
if __name__ == '__main__':
    main()