import math 

print(math.pi)
print(math.e)
print(math.cos(math.pi))
print(math.log(math.e))

print("--------------")
print(math.sin(0))
print(math.sin(math.pi))
print(math.tan(math.pi))

print("--------------")
from math import gcd
print(gcd(64, 24))

print("--------------")
print(math.isclose(3.0, 2.9999, rel_tol=1e-4))
print(math.isclose(3.0, 2.9999, rel_tol=1e-5))
print(math.isclose(3.0, 2.9998, abs_tol=0.0002))
print(math.isclose(3.0, 2.9998, abs_tol=0.0001))
 
print("--------------")
print(math.isclose(0.3, 0.1 * 3))


