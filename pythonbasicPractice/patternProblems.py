# Write a program to print the following number pattern using a loop.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end="")
    print("")

# Print the following pattern
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
