# Print First 10 natural numbers using while loop

def first10_natural_numbers():
    count = 0
    while count <= 10:
        print(count)
        count = count + 1


# first10_natural_numbers()

# Calculate the sum of all numbers from 1 to a given number
def sum_of_entered_number(number):
    sum = 0
    for i in range(1, number + 1):
        sum = sum + i
    print(sum)


# sum_of_entered_number(10)
# Write a program to display only those numbers from a list that satisfy the following conditions

# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop
def list_nums(numbers):
    for i in numbers:
        if i > 500:
            break
        if i > 150:
            continue
        if i % 5 == 0:
            print(i)


# list_nums([12,15,23,27,30,45,155,60,525,21,20])
# Count the total number of digits in a number
def count_digit(number):
    counter = 0
    while number != 0:
        number = number // 10
        counter += 1
    print(counter)


# count_digit(1234)
# Print list in reverse order using a loop
list = [1, 2, 3, 4, 6]
# print(list[-1::-1]) reverse list
new_list = reversed(list)


def reverse_list(list):
    new_list = reversed(list)
    for i in new_list:
        print(i)


# reverse_list(list)

list1 = [10, 20, 30, 40, 50]


# get list size
# len(list1) -1: because index start with 0
# iterate list in reverse order
# star from last item to first
def reverse_list1(list1):
    size = len(list1) - 1
    for i in range(size, -1, -1):
        print(list1[i])


# reverse_list1(list1)
#  Display numbers from -10 to -1 using for loop
def looping_negative():
    for i in range(-10, 0):
        print(i)


# looping_negative()

# Use else block to display a message “Done” after successful execution of for loop
def successful_execution():
    for i in range(5):
        print(i)
    else:
        print("done!")


# successful_execution()

# Write a program to display all prime numbers within a range
def Prime_number(n1, n2):
    for i in range(n1, n2 + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                print(i)


#Prime_number(25, 50)

# Print First 10 natural numbers using while loop
def first_natural():
    count = 0
    while count < 10:
        count += 1
        print(count)


print(first_natural())


# Write a program to print the following number pattern using a loop.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
def number_pattern():
    row = 5
    for i in range(1, row + 1, 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print("")


print(number_pattern())


# Calculate the sum of all numbers from 1 to a given number
def total_number(num):
    addition_num = 0
    for i in range(num + 1):
        addition_num += i
    print(addition_num)


print(total_number(10))


# Write a program to print multiplication table of a given number

def multiplication_table(num):
    for i in range(1, 11, 1):
        print(num * i)


print(multiplication_table(2))


# Display numbers from a list using loop
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop

def divisible_by_five(nums):
    for i in nums:
        if i > 150:
            continue
        elif i > 500:
            break
        elif i % 5 == 0:
            print(i)


print(divisible_by_five([12, 75, 150, 180, 145, 525, 50]))


# Count the total number of digits in a number

def count_total_number(num):
    count = 0
    while num != 0:
        count += 1
        num = num//10
    print(count)


print(count_total_number(3452))

# Write a program to use for loop to print the following reverse number pattern



