# Calculate the multiplication and sum of two numbers
# Given two integer numbers return their product only if the product is equal to or lower than 1000,
# else return their sum.

def sumOrProduct(n1, n2):
    if n1 * n2 < 1000:
        return n1 * n2
    else:
        return n1 + n2


# n1 = int(input("Enter a number : "))
# n2 = int(input("Enter a number : "))
# val = sumOrProduct(n1, n2)
# print(val)


# Write a program to iterate the first 10 numbers and in each iteration, print the sum of
# the current and previous number.

def sumOfCurrentAndPreviousNumber():
    previous_num = 0
    for i in range(1, 11):
        current_num = previous_num + i
        sum = previous_num + current_num
        print("Previous num :", previous_num, ",", "Current num :", current_num, ",", "sum:", sum)
        previous_num = i


# sumOfCurrentAndPreviousNumber()


# Write a program to accept a string from the user and display characters that are present at
# an even index number.
def stringEven(string1):
    for i in range(0, len(string1) - 1, 2):
        print(string1[i])
    # or
    return string1[0::2]


# string1 = input("Enter your name : ")
# str1 = stringEven(string)
# print(str1)


# Write a program to remove characters from a string starting from zero up to n and return a new string.
def removeChar(characters, n):
    return characters[n:]


# characters = input("enter your word: ")
# n = int(input("enter you number: "))
# chars = removeChar(characters, n)
# print(chars)

# Write a function to return True if the first and last number of a given list is same.
# If numbers are different, then return False.

def firstNLastNum(list1):
    if list1[0] == list1[-1]:
        return True
    else:
        return False


list1 = [1, 2, 3, 4, 5, 1]
check = firstNLastNum(list1)


# print(check)


# Return the count of a given substring from a string.

def count_sub_string(str1, sub_str):
    count = str1.count(sub_str)
    print(count)


# str1 = input("Enter any senteence : ")
# sub_str = input("Enter a word from the sentence : ")
# count_sub_string(str1, sub_str)


# Check Palindrome Number
def palindrome(number):
    original_num = number
    # reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    # check numbers
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")


# palindrome(121)
# palindrome(125)


# Given a two list of numbers, write a program to create a new list such that the new list should
# contain odd numbers from the first list and even numbers from the second list.

def new_list(list1, list2):
    newList = []
    for i in list1:
        if i % 2 == 1:
            newList.append(i)
    for j in list2:
        if j % 2 == 0:
            newList.append(j)
    print(newList)


list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]


# new_list(list1, list2)


# Print multiplication table form 1 to 10

def tableFrom1To10():
    for i in range(1, 11):
        print("the table of ", i, "is :")
        for j in range(1, 11):
            table = i * j
            print(table, end=" ")
        print("")


# tableFrom1To10()


# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

def exponent(base, exp):
    if exp > 0:
        value = base ** exp
        print(value)
    # or
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    print(base, "raises to the power of", exp, "is: ", result)


# exponent(5, 4)
# exponent(2, 3)
