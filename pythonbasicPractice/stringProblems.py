# Create a string made of the first, middle and last character
def new_str(string):
    first_letter = string[0]
    middle_letter = string[len(string) // 2]
    last_letter = string[len(string) - 1]
    print(first_letter + middle_letter + last_letter)


# new_str("raina")
# Create a string made of the middle three characters
def middle_character(string):
    a = len(string) // 2
    middle_letter = string[a]
    middle_letter_b = string[a - 1]
    middle_letter_a = string[a + 1]

    print(middle_letter_b + middle_letter + middle_letter_a)


# middle_character("raina")

# Append new string in the middle of a given string
# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in
# the middle of s1.
def new_string(s1, s2):
    mid_index = len(s1) // 2
    new_strinng = s1[0:mid_index] + s2 + s1[mid_index:]
    print(new_strinng)


# new_string("hasan","raina")
# Create a new string made of the first, middle, and last characters of each input string
def new_word(s1, s2):
    a = len(s1)
    b = len(s2)
    n_word = s1[0] + s2[0] + s1[a // 2] + s2[b // 2] + s1[a - 1] + s2[b - 1]
    print(n_word)


# new_word("america","japan")
# ******
# Arrange string characters such that lowercase letters should come first
# str1 = PyNaTive
# Expected Output: yaivePNT
def arrange_string(string):
    lower = []
    upper = []
    for char in string:
        if char.islower():
            lower.append(char)
        else:
            upper.append(char)
    new_s = ''.join(lower + upper)  # ''.join() this function will join the letters.
    print(new_s)  # if we input , or space or anyting in between '' then will show up in between.


# arrange_string("PyNaTive")

# ******
# Count all letters, digits, and special symbols from a given string
def count_l_d_ss(string):
    char = 0
    digit = 0
    special_symbol = 0
    for i in string:
        if i.isalpha():
            char += 1
        elif i.isdigit():
            digit += 1
        else:
            special_symbol += 1
    print(char)
    print(digit)
    print(special_symbol)


# count_l_d_ss("P@#yn26at^&i5ve")

# Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced
# if all the characters in the s1 are present in s2. The character’s position doesn’t matter.
def s1_in_s2(s1, s2):
    if s1 in s2:
        print(True)
    else:
        print(False)


# s1_in_s2("yf", "python")


# or a better solution
def string_balance_test(s1, s2):
    flag = True
    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
    return flag


# print(string_balance_test("yor", "python"))

# Find all occurrences of a substring in a given string by ignoring the case
def count_substring(sentences, sub_string):
    temp_str = sentences.lower()
    count = temp_str.count(sub_string.lower())  # using count(). it'll count the string or sub string
    print("the number of sub string in sentences : ", count)  # that we put in between the parentheses


sentences = "Welcome to USA. the city is awesome, isn't it?"
sub_string = "USA"


# count_substring(sentences, sub_string)

# Calculate the sum and average of the digits present in a string
def sum_average_of_str(str1):
    sum = 0
    count = 0
    for char in str1:
        if char.isdigit():
            sum += int(char)
            count += 1
        else:
            continue
    average = sum / count
    print(sum)
    print(average)


# sum_average_of_str("raina1998")

# or another way of solution
# import re
#
# input_str = "PYnative29@#8496"
# digit_list = [int(num) for num in re.findall(r'\d', input_str)]
# print('Digits:', digit_list)
#
# # use the built-in function sum
# total = sum(digit_list)
#
# # average = sum / count of digits
# avg = total / len(digit_list)
# print("Sum is:", total, "Average is ", avg)

# Write a program to count occurrences of all characters within a string
# Given:str1 = "Apple"
# Expected Outcome: {'A': 1, 'p': 2, 'l': 1, 'e': 1}

def dict_str(string):
    char_dict = dict()
    for char in string:
        count = string.count(char)
        char_dict[char] = count  # as we know in dictionary , var[key] = value
    print(char_dict)


# dict_str("happy")


# Reverse a given string
def reverse_string(string):
    print(string[::-1])


# reverse_string("happy")


# or another way
def rev_str(string):
    str1 = ''.join(reversed(string))
    print(str1)


# rev_str("raina")

# Find the last position of a given substring
def last_position_str(str, sub_str):
    n_str = str.lower()
    n_sub_str = sub_str.lower()
    position = n_str.rfind(n_sub_str)
    print(position)


# last_position_str("I an Raina.", "rai")

# Split a string on hyphens
# Given: str1 = Emma-is-a-data-scientist
# Expected Output:
# Emma
# is
# a
# data
# scientist
def split_str(string):
    n_str = string.split("-")
    print(n_str)
    for item in n_str:
        print(item)


# split_str("rai-ali-azad")

# Remove empty strings from a list of strings
# Given: str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# Expected Output: ['Emma', 'Jon', 'Kelly', 'Eric']
def remove_emp_str(str_list):
    res_list = []
    for s in str_list:
        # check for non empty string
        if s:
            res_list.append(s)
    print(res_list)


# remove_emp_str(["Emma", "Jon", "", "Kelly", None, "Eric", ""])
# or
def filter_list(string):
    # use built-in function filter to filter empty value
    new_str_list = list(filter(None, string))
    print(new_str_list)


# filter_list(["Emma", "Jon", "", "Kelly", None, "Eric", ""])

# Remove special symbols / punctuation from a string
# Given: str1 = "Jo/*n is @developer & musician"
# Expected Output: "Jon is developer musician"

def rmv_str(str1):
    n_str_list = []
    for char in str1:
        if char.isalpha():
            n_str_list.append(char)
    n_str = ''.join(n_str_list)
    print(n_str)


# rmv_str("Jo/*n is @developer & musician")

# Use string functions translate() and maketrans().
# The string.punctuation constant contain all special symbols.
import string

str1 = "/*Jon is @developer & musician"
new_str = str1.translate(str.maketrans('', '', string.punctuation))
print(new_str)

# Using regex replace pattern in a string
import re

# replace special symbols with ''
res = re.sub(r'[^\w\s]', '', str1)
print("New string is ", res)


# Removal all characters from a string except integers
# new rules
# # Using list comprehension + join() + isdigit()
# res = "".join([item for item in str1 if item.isdigit()])
def only_int(string):
    int_str = []
    for char in string:
        if char.isdigit():
            int_str.append(char)
    print(''.join(int_str))


only_int(" raina 1998 . hasan 10th dec")


# Find words with both alphabets and numbers
# Given: str1 = "Emma25 is Data scientist50 and AI Expert"
# Expected Output:
# Emma25
# scientist50
def alpha_with_int(str1):
    alpha_int = []
    # split string on whitespace
    temp = str1.split()
    # Words with both alphabets and numbers
    # isdigit() for numbers + isalpha() for alphabets
    # use any() to check each character
    for item in temp:
        if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
            alpha_int.append(item)
    for i in alpha_int:
        print(i)


alpha_with_int("Emma25 is Data scientist50 and AI Expert")

# Replace each special symbol with # in the following string
str1 = '/*Jon is @developer & musician!!'
for i in string.punctuation:
    str1 = str1.replace(i, "#")
print(str1)


