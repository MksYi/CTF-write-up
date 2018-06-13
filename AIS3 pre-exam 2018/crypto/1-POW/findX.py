#!/usr/bin/python3
from pwn import *
import math
ip   = '104.199.235.135'
prot = 20000

r = remote(ip, prot)

print(r.recvline())
print(r.recvline())
data = r.recvline()
print(data)
data = data.split(' ')[4]
data = data.strip('\'')
anwser = ''
for i in range(100000000):
    if hashlib.sha256((data + str(i)).encode('utf-8')).hexdigest()[:6] == '000000':
        anwser = (data + str(i))
        break
print(anwser)
print(r.sendline(anwser))
print(r.recvline())