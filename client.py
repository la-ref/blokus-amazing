from datetime import datetime
import socket,pickle
import struct
import threading
import time
from config import config
import ast

class Client:

    PORT = 5005

    def __init__(self,nom):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.nom = nom
        self.id = 0
        self.error = False
        try:
            self.s.connect((config.Config.controller.onlineGame.ip, int(config.Config.controller.onlineGame.port)))
        except:
            self.error = True
            config.Config.controller.leaveOnline(send=False,error="Erreur fatale : Aucun serveur trouvé")
            
    def getId(self):
        self.send("blokus."+self.nom)
        self.id = int(self.oneReceive())
        return self.id
    
    def stopSock(self):
        try:
            self.s.shutdown(socket.SHUT_WR)
            self.s.close()
        except:
            pass
    
    def recvall(self,sock, count):
        buf = b''
        while count:
            newbuf = sock.recv(count)
            if not newbuf: return None
            buf += newbuf
            count -= len(newbuf)
        print(buf)
        return buf
    
    def convertJson(self,msg):
        return ast.literal_eval(str(msg))

    def receive(self):
        while not self.error:
            try:
                lengthbuf = self.recvall(self.s, 4)
                length, = struct.unpack('!I', lengthbuf)
                data = self.recvall(self.s, length)
                
                if len(data) == 0:
                    self.error = True
                    config.Config.controller.leaveOnline(send=False,error="Erreur fatale : Serveur déconnecté")
                    break
                else:
                    val = str(data.decode())
                    print(val,"§§§§§§§§§§§§§§§")
                    if "errormsg." in val:
                        val = val.replace("errormsg.", '')
                        config.Config.controller.leaveOnline(send=False,error=val)
                    if config.Config.controller.currentPage == "lobbyOnline":
                        if "userNames." in val:
                            val = val.replace("userNames.", '')
                            config.Config.controller.changeUserNames(self.convertJson(val))
                        elif "launchGame." in val:
                            val = val.replace("launchGame.", '')
                            config.Config.controller.launchGame(self.convertJson(val))
                    if config.Config.controller.currentPage == "GameInterfaceOnline":
                        if "placement." in val:
                            val = val.replace("placement.", '')
                            config.Config.controller.placement(self.convertJson(val))
                        if "refreshgame." in val:
                            val = val.replace("refreshgame.", '')
                            config.Config.controller.placement(self.convertJson(val))
            except:
                self.error = True
                print(("error receive", "({}) : Server has been disconnected.\n".format("rip")))
                config.Config.controller.leaveOnline(send=False,error="Erreur fatale : Serveur déconnecté")
                break
            
    def oneReceive(self):
        try:
            self.s.settimeout(10.0)
            
            lengthbuf = self.recvall(self.s, 4)
            length, = struct.unpack('!I', lengthbuf)
            data = self.recvall(self.s, length)
            
            self.s.settimeout(None)
            print("MY DATA ", data)
            if len(data) == 0:
                self.error = True
                config.Config.controller.leaveOnline(send=False,error="Erreur fatale : Serveur déconnecté")
            else:
                return data.decode()
        except:
            self.error = True
            print(("error receive", "({}) : Server has been disconnected.\n".format("rip")))
            config.Config.controller.leaveOnline(send=False,error="Erreur fatale : Serveur déconnecté")
            return None
                
    def send(self,msg = None):
        now = str(datetime.now())[:-7]
        sended = False
        try:
            self.s.sendall(struct.pack("!I",len(bytes(msg, "utf-8"))))
            self.s.sendall(bytes(msg, 'utf-8'))
            print("Moi - {}".format(msg))
            sended = True
        except:
            self.error = True
            print(("error send", "({}) : Server has been disconnected.\n".format(now)))
            config.Config.controller.leaveOnline(send=False,error="Erreur fatale : Serveur déconnecté")
        return sended