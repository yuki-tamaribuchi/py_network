from ethernet import EthernetFrame
from ip import IPv4Packet

if __name__ == "__main__":
	eth = EthernetFrame()
	ip = IPv4Packet(data=b"", src="192.168.11.14")