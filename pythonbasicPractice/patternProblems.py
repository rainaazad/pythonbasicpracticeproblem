# Write a program to print the following number pattern using a loop.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print("")

print("................")
# Print the following pattern
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j, end=" ")
    print("")
print(".....................")
# Print downward Half-Pyramid Pattern with Star
# * * * * *
# * * * *
# * * *
# * *
# *
for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")


