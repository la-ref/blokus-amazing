import scapy.all as scapy
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("51.75.249.26",27025))
print(s)