words = ['разработка', 'сокет', 'декоратор', 'содержимое']

for s in words:
    res = ''.join(r'\u{:04X}'.format(ord(chr)) for chr in s)
    print("The unicode converted String : " + str(res))
    s =+ 1

