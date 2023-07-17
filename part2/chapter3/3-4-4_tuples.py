x = (1, 2, 3, "a", "b", "c")
print(x[0])
print(x[3])

 # x[3] = "2"

print("---------------")
y = (1)
print(type(y))
y = (1,)
print(type(y))

print("---------------")
places = {
  (35.312656, 139.533062): '鎌倉 長谷寺', 
  (51.500485, -0.124342): 'London Palace of Westminster',
}
print(places)
print(places[35.312656, 139.533062])
print(places[51.500485, -0.124342])
# print(places['鎌倉 長谷寺'])



