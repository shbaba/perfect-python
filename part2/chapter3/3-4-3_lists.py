x = [1, 2, 3.0, "a", "b", "c"]

for i in range(6):
  print(str(i) + ":" + str(x[i]))

for i in range(-6, 0):
  print(str(i) + ":" + str(x[i]))

print("-----------")
print(x[1:2])
print(x[1:4])
print(x[2:-1])
print(x[-3:-1])
print(x[-1:-3])
print(x[-3:-7])

print("-----------")
print(x[1:])
print(x[:3])
print(x[:-2])
print(x[:])

print("-----------")
for item in x:
  print(item)

print("-----------")
for item in x[3]:
  print(item)

print("-----------")
x = []
x.append('spam')
print(x)
x.append('eggs')
print(x)

print("-----------")
x.remove('eggs')
print(x)
x.remove('spam')
print(x)

# x.remove('abc')

print("-----------")
x = ['spam', 'eggs']
x[1] = 'hoge'
print(x)

print("-----------")
x = [1, 2, 3, 4, 5]
print(x[1:4])

x[1:4] = ["spam", "eggs"]
print(x)

print("-----------")
x = [1, 2, 3]
print(x.reverse())
print(x)

print("-----------")
x = [1, 0, 1, 7, 4, 1, 4, 7, 3, 3]
print(x.sort())
print(x)

print("-----------")
print([i for i in range(10) if i % 2 == 0])
print(i)

print("-----------")
print([str(i) for i in range(10) if i % 2 == 0])
print(i)


