x = 'テスト'.encode('utf8')
# x.decode('cp932')

# Traceback (most recent call last):
#   File "/Users/babaShumpei/Desktop/work/shbaba/perfect-python/part2/chapter3/3-4-1_sequence_str.py", line 2, in <module>
#     x.decode('cp932')
# UnicodeDecodeError: 'cp932' codec can't decode byte 0x86 in position 2: illegal multibyte sequence

print(x.decode())

x = 'テスト'.encode()
print(x.decode('utf8'))


print("---------------")
name = 'Taro'
print('hello ' + name + ' san')

print("---------------")
print('%s, %s!' % ('hello', 'world',))

print("---------------")
a = 2
b = 3
print('%s * %d = %d' %(a, b, a * b,))

print("---------------")
print('%03d' %1)

print('%10.3f' % 2.1)

print('%d%%' % 100)

print("---------------")
print('%(name)sは%(year)d歳です。' % {'name': 'Tom', 'year': 20})

print("---------------")
print('{} {}!'.format('hello', 'world'))

print("---------------")
print('{1} {0}!'.format('hello', 'world'))

print("---------------")
print('{name} is {year} years old.'.format(name='Okuizumi', year=38))

print("---------------")
print('{!a}'.format('非ascii文字なのでescape'))

print("---------------")
print('{:^20}'.format('123456789'))
print('{:*>20}'.format('123456789'))
print('{:,}'.format(123456789))

print("---------------")
name = 'One'
age = 23
print(f'名前: {name:>10}')
print(f'年齢: {age:>10}')

print("---------------")
boy = 18
girl = 22
print(f'{boy} + {girl} = {boy + girl}')

print("---------------")
s = 'spam'
print(id(s))
s = 'egg'
print(id(s))

print("---------------")
a = 'spam'
b = 'spam'
c = 'spam'
print(id(a), id(b), id(c))

print("---------------")
print('spam'.lower() is 'spam'.lower())
import sys
print(sys.intern('spam'.lower()) is sys.intern('spam'.lower()))



