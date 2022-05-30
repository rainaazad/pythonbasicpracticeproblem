animals = {"tiger", "dog", "elephant", "cat", "zebra", "lion"}
# remove item from set
animals.remove("cat")
print("1.", animals)
animals.discard("lion")
print("2.", animals)
# animals.pop()  # randomly remove any item from set
# print(animals)
# add item or items in set
animals.add("lion")
print("3.", animals)
animals.update(["giraffe","fox"], {"dog"})
print("4.", animals)
# others method in set
zoo = animals.copy()
print("#.", zoo)
dif = zoo.difference({"snake", "crocodile", "birds", "tiger", "lion"})
print("5.", dif)
zoo = zoo.union({"snake", "crocodile", "birds", "tiger", "lion"})
print("6.", zoo)
print("#. Common of two set :", zoo.intersection(animals))

