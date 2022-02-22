import struct
import binascii
import socket

class IPv4Packet:
	version_and_ihl = 0b01000101
	flag_and_flag_offset = 0x00
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
		src_ip_addr = int("".join([bin(int(x)+256)[3:] for x in self.src.split(".")]),2)
		dst_ip_addr = int("".join([bin(int(x)+256)[3:] for x in self.dst.split(".")]),2)

		header_sum =  self.version_and_ihl + self.dscp + self.total_length + self.identification + self.flag_and_flag_offset + self.ttl + self.protocol + src_ip_addr + dst_ip_addr
		check_sum = 0xFFFF - header_sum
		print(check_sum)

				

		self.raw = struct.pack(
			"!2B3h2Bh2L",
			self.version_and_ihl, #1byte
			self.dscp, #1byte
			self.total_length, #2bytes
			self.identification, #2bytes
			self.flag_and_flag_offset, #2bytes
			self.ttl, #1byte
			self.protocol, #1byte
			check_sum, #2bytes
			src_ip_addr, #4bytes
			dst_ip_addr, #4bytes
		)
		print(self.raw)
		print(len(self.raw))
