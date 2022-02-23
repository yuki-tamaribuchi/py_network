import struct
import binascii
import socket

class IPv4Packet:
	version_ihl_dscp = 0b0100010110000000
	flag_and_flag_offset = 0x00
	protocol = 0x06
	ttl = 255
	ttl_protocol = (ttl<<4) + protocol


	def __init__(self, data, src, dst="255.255.255.255"):
		self.data = data
		self.src = src
		self.dst = dst
		self.identification = 0
		self.protocol = 0x06
		self.options = None
		self.total_length = 0x5 + len(self.data)
		self.raw = None
		self.assemble_ip_fields()

	def assemble_ip_fields(self):
		src_ip_addr = int("".join([bin(int(x)+256)[3:] for x in self.src.split(".")]),2)
		dst_ip_addr = int("".join([bin(int(x)+256)[3:] for x in self.dst.split(".")]),2)

		header_sum =  self.version_ihl_dscp 
		+ self.total_length
		+ self.identification
		+ self.flag_and_flag_offset
		+ self.ttl_protocol
		+ int(bin(src_ip_addr)[2:18], 2)
		+ int(bin(src_ip_addr)[18:] ,2)
		+ int(bin(dst_ip_addr)[2:18], 2)
		+ int(bin(dst_ip_addr)[18:], 2)
		
		
		check_sum = 0xFF - header_sum

				

		self.raw = struct.pack(
			"!6h2L",
			self.version_ihl_dscp, #2byte
			self.total_length, #2bytes
			self.identification, #2bytes
			self.flag_and_flag_offset, #2bytes
			self.ttl_protocol, #2bytes
			check_sum, #2bytes
			src_ip_addr, #4bytes
			dst_ip_addr, #4bytes
		)

	def get_ip_packet(self):
		return self.raw + self.data