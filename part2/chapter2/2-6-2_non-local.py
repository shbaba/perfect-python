def counter():
	count = 0
	def _counter():
		nonlocal count
		count += 1
		return count
	return _counter

c = counter()
print(c())
print(c())
print(c())
