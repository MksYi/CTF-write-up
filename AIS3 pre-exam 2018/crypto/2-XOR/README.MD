# AIS3 pre-exam 2018: XOR

**Category:** Crypto  
**Points:** 2  

## Write-up

提供了 [encrypt.py](./encrypt.py-09f175c1a9aa1e31ec613dfc6f1c1bb8c8777504) 加密器以及 [flag-encrypted](flag-encrypted-511ab4a9fd7bb2d216ab5b5afa7fae5742eef94e) 密文。  


**加密程序**
``` python
def extend(key, L):
    kL = len(key)
    return key * (L // kL) + key[:L % kL]

def xor(X, Y):
    return bytes([x ^ y for x, y in zip(X, Y)])

key = os.urandom(random.randint(8, 12))
plain = flag + key
key = extend(key, len(plain))
cipher = xor(plain, key)
```



**原理探討**

flag = 'AIS{XXXXXXXXXXXXX...'  
key = '???????'  
plaintext = '????????'  

```python
def xor(s1,s2):
    return ''.join(chr(a ^ ord(b)) for a,b in zip(s1,s2))

def repeat(s, l):
    return (s*(int(l/len(s))+1))[:l]

with open('flag-encrypted-511ab4a9fd7bb2d216ab5b5afa7fae5742eef94e', 'rb') as data:
    cipher_and_key = data.read()
    print('cipher_and_key_Lenght: ', len(cipher_and_key))
    for i in range(len(cipher_and_key)):
        if i % 15 == 0:
            print()
        print(cipher_and_key[i], end=' ')
'''
cipher_and_key_Lenght: 161
 87  64  47 244 166  44  79 226 211 190  95 103  92 166 144
 42  92 251 196 203  54  36  92 144 181 123 122 161 241 204
 68  41  52 166 173  31  75 252 244 223  98  57  17 136 143
 61  30 229 135 166  89  92  92 170 136  60  90 178 247 173
 38  68  21 180 238 111  99 215 135 144 120  58  92 179 149
  6  64 245 137 223  66  65  72 147 253  54  97 231 135 168
127  69  48 231 174  59 111 203 135 168 126 102  92 158 237
 26  14 166 245 186  56  41  50 168 169 111 111 178 215 186
 68 111  25 164 169 111  93 221 150 155  95  76  46 235 253
 45  91 198 135 203  54 110  51 136 153 111  99 211 201 209
107  31 117 187  26 146  97 188  53  88 233
'''

xor_all = 0
for i in range(len(cipher_and_key) - 1, -1, -1):
    xor_all ^= cipher_and_key[i]
    if xor_all == 0:
        flag_len = i
        key_len = len(cipher_and_key) - i
        print('flag length:', flag_len)
        print('key length:', key_len)
        break

'''
-------->>
|[160]|[159]|[158]|[157]|[156]|[155]|[154]|[153]|[152]|[151]|
| 233 |  88 |  53 | 188 |  97 | 146 |  26 | 187 | 117 |  31 |
|   0 | 233 | 177 | 132 |  56 |  89 | 203 | 209 | 106 |  31 | XOR
+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+----
| 233 | 177 | 132 |  56 |  89 | 203 | 209 | 106 |  31 |   0 |
-------------------------------------------------------------

flag_len = 151
key_len  = len(cipher_and_key) - i
     10  = 161 - 151
'''
xored_flag = cipher_and_key[:flag_len]
xored_key = cipher_and_key[flag_len:]

print('xored_flag: ')
for i in range(len(xored_flag)):
    if i % 15 == 0:
        print()
    print(xored_flag[i], end=' ')
print('xored_key: ')
for i in range(len(xored_key)):
    if i % 15 == 0:
        print()
    print(xored_key[i], end=' ')  

'''
xored_flag: 
 87  64  47 244 166  44  79 226 211 190  95 103  92 166 144
 42  92 251 196 203  54  36  92 144 181 123 122 161 241 204
 68  41  52 166 173  31  75 252 244 223  98  57  17 136 143
 61  30 229 135 166  89  92  92 170 136  60  90 178 247 173
 38  68  21 180 238 111  99 215 135 144 120  58  92 179 149
  6  64 245 137 223  66  65  72 147 253  54  97 231 135 168
127  69  48 231 174  59 111 203 135 168 126 102  92 158 237
 26  14 166 245 186  56  41  50 168 169 111 111 178 215 186
 68 111  25 164 169 111  93 221 150 155  95  76  46 235 253
 45  91 198 135 203  54 110  51 136 153 111  99 211 201 209
107
xored_key:
31 117 187 26 146 97 188 53 88 233
'''

key_num_lst = [0] * key_len
# flag may start with 'AIS3{', and we only need the first letter
key_num_lst[0] = ord('A') ^ xored_flag[0]
'''
key_num_lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
key_num_lst[0] = 65 ^ 87 = 22
'''
pre_idx = 0
shift = key_len - flag_len
idx = (pre_idx + shift) % key_len
'''
shift = 10 - 151 = -141
idx = (0 + (-141)) % 10 = 9
'''
while key_num_lst[idx] == 0:
    key_num_lst[idx] = key_num_lst[pre_idx] ^ xored_key[idx]
    pre_idx = idx
    idx = (pre_idx + shift) % key_len
key = ''.join(map(chr, key_num_lst))
'''
idx                  9   8   7   6   5   4   3    2   1   0 
key_num_lst[idx]   255 167 146  46  79 221 199  124   9  22
'''
print('key:', key)
flag = xor(xored_flag, repeat(key, len(xored_flag)))
print('flag:', flag)
```
解題腳本 `decrypto.py`

`AIS3{captAIn aMeric4 - Wh4T3V3R HapPenS t0mORr0w YOU mUst PR0Mis3 ME on3 tHIng. TH4T yOu WiLL stAY Who Y0U 4RE. Not A pERfect sO1dIER, buT 4 gOOD MAn.}`

**解題參考:**  
>[[CSAW CTF Qualification Round 2017] - Another Xor (Crypto 100)](https://andyw330.github.io/2017/09/28/CSAW-CTF-Qualification-Round-2017-Another-Xor-Crypto-100/)

