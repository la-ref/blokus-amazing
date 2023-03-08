import scapy.all as scapy
import socket

for i in range(200):
    for y in range(200):
        pack = scapy.IP(src="localhost", dst="localhost") / scapy.TCP(sport=57220, dport=5005,seq=i,ack=y,flags="S") / "Fuck you"
        scapy.send(pack)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("localhost",5005))
        p = scapy.IP(dst="localhost")/scapy.TCP(flags="S", sport=scapy.RandShort(),dport=5005)/"Hallo world!"
        q = scapy.IP(dst="localhost")/scapy.TCP(flags="S", sport=57220,dport=5005)/"Hallo world!"
        scapy.send(p)
        scapy.send(q)