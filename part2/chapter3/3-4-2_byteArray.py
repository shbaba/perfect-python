ba1 = bytearray()
ba1.append(115)
ba1.append(112)
ba1.append(97)
ba1.append(109)
print(ba1)

print("----------")
ba2 = bytearray([115, 112, 97, 109])
print(ba2)

print("----------")
ba3 = bytearray('日本語', 'utf8')
print(ba3)

print("----------")
ba4 = bytearray(b'egg')
print(ba4)

print("----------")
ba5 = bytearray(128)
print(ba5)

print("----------")
ba_nihongo = bytearray('スパム', 'utf8')
print(ba_nihongo)

print(len(ba_nihongo))

print(ba_nihongo.decode())

print("----------")
ba = bytearray('spam', 'utf8')
ba[1] = 104
print(b'spam')

