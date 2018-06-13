#!/usr/bin/python3
# Reference:
# https://andyw330.github.io/2017/09/28/CSAW-CTF-Qualification-Round-2017-Another-Xor-Crypto-100/

import os
import random

def xor(s1,s2):
    return ''.join(chr((a) ^ ord(b)) for a,b in zip(s1,s2))
def repeat(s, l):
    return (s*(int(l/len(s))+1))[:l]

key=[0]*100
flag = ''
xor_all = 0

with open('flag-encrypted-511ab4a9fd7bb2d216ab5b5afa7fae5742eef94e', 'rb') as data:
	flag = data.read()
	for i in range(len(flag) - 1, -1, -1):
		xor_all ^= flag[i]
		if xor_all == 0:
			flag_len = i
			key_len = len(flag) - i
			print('flag length:', flag_len)
			print('key length:', key_len)
			break	

xored_flag = flag[:flag_len]
xored_key = flag[flag_len:]
key_num_lst = [0] * key_len
key_num_lst[0] = ord('A') ^ xored_flag[0]
shift = key_len - flag_len
pre_idx = 0
idx = (pre_idx + shift) % key_len
while key_num_lst[idx] == 0:
    key_num_lst[idx] = key_num_lst[pre_idx] ^ xored_key[idx]
    pre_idx = idx
    idx = (pre_idx + shift) % key_len
key = ''.join(map(chr, key_num_lst))
print('key:', key)
flag = xor(xored_flag, repeat(key, len(xored_flag)))
print('flag:', flag)
print(key)
