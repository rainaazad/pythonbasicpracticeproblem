# create a programme to check a number is positive or negative or 0.

def check_number(number):
    if number < 0:
        print(number, "is a negative number")
    elif number == 0:
        print(number, "is zero")
    else:
        print(number, "is a positive number")


# check_number(-12)


count = 5
while count <= 10:
    # print(count)
    count = count + 1


# can you modify the multiplication table program so that we get
# a multiplication table from 10 to 1 insted of 1 to 10?
def multiplication_table(number):
    count = 10
    while count > 0:
        product = number * count
        print(number, "*", count, "=", product)
        count = count - 1


# multiplication_table(2)

# can you create a program to find the sum of numbers from 1 to 100?
def sumofnumbers(number):
    sum = 0
    for i in range(1, number + 1):
        sum = sum + i
    print(sum)


# sumofnumbers(100)

# can you create a program so that all the items of the languages list are printed except Swift and c++
# languages = ["python", "java", "swift", 'C','C++']

def languages_list(languages):
    for language in languages:
        if language == "C++" or language == "swift":
            continue
        else:
            print(language)


# languages_list(['python','java','swift','C','C++'])

# suppose you just attend a university examination. the marks are obtained in various subjects are stored in
# a list like this : marks = [ 55, 64, 75, 80, 65]
# you want to find the average marks you obtained in the exam . and , based on the average marks  you want to
# find out your grade. the grading rule  is like this:
# you will get grade A if the average marks is equal to or above 80
# you will get grade B if the average marks is equal to or above 60 but less than 80
# you will get Grade C if the average marks is equal to or above 50 and less than 60
# you will get grade F  if the average marks is less than 50

def Gradeoftheaveragemarks(marks):
    average_marks = sum(marks) / len(marks)
    print(average_marks)
    if 0 >= average_marks < 50:
        print("Grade F")
        print("sorry, you have failed the exam")
    elif 50 <= average_marks < 60:
        print("Grade C")
        print("Congrats, you have passed the exam")
    elif 60 <= average_marks < 80:
        print("Grade B")
        print("Congrats, you have passed the exam")
    elif average_marks >= 80:
        print("Grade A")
        print("Congrats , you nailed the exam")
    else:
        print("Absent")


marks = [55, 64, 75, 80, 65]

Gradeoftheaveragemarks(marks)

#
