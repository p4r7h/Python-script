import binascii
from binascii import unhexlify

def xor(s1, s2):
    return ''.join(format(int(a, 16) ^ int(b, 16), 'x') for a,b in zip(s1,s2))
KEY1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
KEY2 = xor("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e", KEY1)
KEY3 = xor("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1", KEY2)
KEY4 = xor(KEY3 ,xor(KEY1, KEY2))
FLAG = xor("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf", KEY4)
print(unhexlify(FLAG))

