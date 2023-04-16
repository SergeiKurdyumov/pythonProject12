import binascii

words = [b'class', b'function', b'method']

for s in words:
    print(type(s), binascii.hexlify(s), len(s))


