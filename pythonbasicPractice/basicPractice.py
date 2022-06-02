var = "have a good day"

print(var[1::-1])  # var[start:: step]
print(var[0::1])
print(var[::])
print(var[::2])
print(var[-1::1])
print(var[-1::-1])
print(var[0::-1])
print(var[::-1])
print(var[-1::])

# explicit continuation
add = 20 + 40 + \
      30 + 10 + \
      60
print(add)
