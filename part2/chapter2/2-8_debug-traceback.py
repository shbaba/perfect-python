def main():
	x = 123
	y = "ほげ"
	print(concat(x, y))

def concat(a, b):
	return str(a) + str(b)

if __name__ == '__main__':
	main()


# Traceback (most recent call last):
#   File "/Users/babaShumpei/Desktop/work/shbaba/perfect-python/part2/chapter2/2-8_debug-traceback.py", line 10, in <module>
#     main()
#   File "/Users/babaShumpei/Desktop/work/shbaba/perfect-python/part2/chapter2/2-8_debug-traceback.py", line 4, in main
#     concat(x, y)
#   File "/Users/babaShumpei/Desktop/work/shbaba/perfect-python/part2/chapter2/2-8_debug-traceback.py", line 7, in concat
#     return a + b
#            ~~^~~
#  TypeError: unsupported operand type(s) for +: 'int' and 'str'

