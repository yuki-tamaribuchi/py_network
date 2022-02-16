import struct
import binascii

class IPv4Packet:
	version_and_ihl = 0x45
	flag_and_identification = 0x00
	dscp = 0b10000000
	ttl = 255


	def __init__(self, data, src, dst="255.255.255.255", identification=0, protocol=0x06, options=None):
		self.data = data
		self.src = src
		self.dst = dst
		self.identification = identification
		self.protocol = protocol
		self.options = options
		self.total_length = 0x5 + len(self.data)
		self.raw = None
		self.assemble_ip_fields()

	def assemble_ip_fields(self):
		self.raw = struct.pack(
			"!3h2l2h",
			self.version_and_ihl,
			self.dscp,
			self.total_length,
			self.identification,
			self.flag_and_identification,
			self.ttl,
			self.protocol,
		)
		print(self.raw)
