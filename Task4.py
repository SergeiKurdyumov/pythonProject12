words = ['разработка', 'администрирование', 'protocol', 'standard']
words_in_bytes = []

for s in words:
    s = s.encode('utf-8')
    words_in_bytes.append(s)
    print(s)

for s in words_in_bytes:
    s = s.decode('utf-8')
    print(s)