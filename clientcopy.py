from datetime import datetime
import socket
import threading
import time
from config import config
import ast

class Client:

    PORT = 5005

    def __init__(self,nom):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.nom = input("Ton pseudo : \n")
        # print("\x1B[F\x1B[2K", end="")
        self.nom = nom
        self.id = 2
        now = str(datetime.now())[:-7]
        self.error = False
        try:
            self.s.connect(("localhost", Client.PORT))
        except ConnectionRefusedError:
            self.error = True
            config.Config.controller.changePage("connexion")
            print("error connect", "({}) : The server is not online.\n".format(now))
            
    def getId(self):
        self.send(self.nom)
        self.id = int(self.oneReceive())
        # if not self.id:
        #     # envoi page d'erreur au client..
        #     return
        return self.id
    
    def stopSock(self):
        try:
            self.s.shutdown(socket.SHUT_WR)
        except:
            config.Config.controller.changePage("Accueil")
            
    
    def convertJson(self,msg):
        #self.send("getUserNames")
        #return ast.literal_eval(str(self.oneReceive()))
        return ast.literal_eval(str(msg))

    def receive(self):
        while not self.error:
            try:
                data = self.s.recv(8192)
                if len(data) == 0:
                    self.error = True
                    self.s.close()
                    break
                else:
                    val = str(data.decode())
                    if config.Config.controller.currentPage == "lobbyOnline":
                        if "userNames." in val:
                            val = val.replace("userNames.", '')
                            config.Config.controller.changeUserNames(self.convertJson(val))
                    print("{}\n".format(val))
            except:
                self.error = True
                print(("error receive", "({}) : Server has been disconnected.\n".format("rip")))
                self.s.close()
                break
            
    def oneReceive(self):
        try:
            self.s.settimeout(10.0)
            data = self.s.recv(8192)
            self.s.settimeout(None)
            print("MY DATA ", data)
            if len(data) == 0:
                self.error = True
                self.s.close()
            else:
                return data.decode()
        except:
            self.error = True
            print(("error receive", "({}) : Server has been disconnected.\n".format("rip")))
            self.s.close()
            return None
                
    def send(self,msg = None):
        now = str(datetime.now())[:-7]
        sended = False
        try:
            self.s.send(bytes(msg, 'utf-8'))
            print("Moi - {}".format(msg))
            sended = True
        except:
            self.error = True
            print(("error send", "({}) : Server has been disconnected.\n".format(now)))
            self.s.close()
        return sended
            
    def inp(self):
        while not self.error:
            msg = input("\n")
            print("\x1B[F\x1B[2K", end="")
            if not self.send(msg):
                break
            

# c1 = Client()
# t1 = threading.Thread(target=c1.receive)
# t1.start()

# t23 = threading.Thread(target=c1.inp)
# t23.start()
