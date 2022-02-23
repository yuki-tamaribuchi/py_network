from ethernet import EthernetFrame
from ip import IPv4Packet

if __name__ == "__main__":
	eth = EthernetFrame()
	eth_frame = eth.get_ehternet_frame()
	ip = IPv4Packet(data=b"", src="192.168.11.14")
	ip_packet = ip.get_ip_packet()
