import binascii
import struct

ETH_P_IP = 0x0800

class EthernetFrame:
	def __init__(self, dst="ff:ff:ff:ff:ff:ff", src="ff:ff:ff:ff:ff:ff", protocol=ETH_P_IP):
		self.dst = dst
		self.src = src
		self.protocol = protocol
		self.raw = None
		self.assemble_eth_fields()

	def assemble_eth_fields(self):
		self.raw = struct.pack(
			# !=Big Endian, 6s=char[] *6, H=unsigned short
			"!6s6sH",
			binascii.unhexlify(self.dst.replace(":", "")),
			binascii.unhexlify(self.src.replace(":", "")),
			self.protocol
		)

	def get_ehternet_frame(self):
		return self.raw