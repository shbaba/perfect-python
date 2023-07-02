import numbers

obj = 1
print(isinstance(obj, numbers.Real))
print(isinstance(obj, numbers.Complex))
print(isinstance(obj, numbers.Rational))

print("---------------")
obj = complex(1, 1)
print(obj)
print(isinstance(obj, numbers.Complex))
print(isinstance(obj, numbers.Rational))
print(isinstance(obj, numbers.Real))


