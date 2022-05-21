# Write a program to check whether a person is eligible for voting or not.
# age = int(input("Enter your age : "))
def vote_approval(age):
    assert age > 0, " stop kidding , age can not be a negative number"
    if age >= 18:
        print("You can vote.")
    else:
        print("Please wait until you turn 18 .")


# vote_approval(age)

# Write a program to check whether a number entered by user is even or odd.

def even_odd(number):
    if number % 2 == 0:
        print(number, "is an even number")
    else:
        print(number, "is an odd number")


# even_odd(56)

#  Write a program to check whether a number is divisible by 7 or not.

def divisible_by_7(number):
    if number % 7 == 0:
        print(number, " is divisible by 7")
    else:
        print(number, "is not divisible by 7")


# divisible_by_7(84)

# Write a program to display "Hello" if a number entered by user is a multiple of five ,
# otherwise print "Bye".

def multipleoffive(number):
    if number % 5 == 0:
        print("hello")
    else:
        print("bye")


# multipleoffive(61)

# Write a program to calculate the electricity bill (accept number of unit from user)
# according to the following criteria :
# unit                                                         price
# First 100 units                                               no charge
# Next 100 units                                              Rs 5 per unit
# After 200 units                                             Rs 10 per unit
# (For example if input unit is 350 than total bill amount is Rs2000)

def electricity_bill(units):
    if units < 100:
        return
    elif units >= 100 and units < 200:
        return units * 5
    elif units >= 200:
        return units * 10


# units = int(input("Enter your units : "))
# print(electricity_bill(units))

# Write a program to display the last digit of a number.

def last_digit_number(number):
    if number % 10 != 0:
        return number % 10
    else:
        return 0


# print(last_digit_number(555670))

# Write a program to check whether the last digit of a number( entered by user ) is
# divisible by 3 or not.

def last_digit_divisible_by3(number):
    if (number % 10) % 3 == 0:
        print("The last digit is divisible by 3")
    else:
        print("The last digit is not divisible by 3")


# last_digit_divisible_by3(49)

# Write a program to check whether a year is leap year or not.
def leap_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        if year % 4 == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")


# year = int(input("Enter the year: "))
# leap_year(year)

#  Accept any city from the user and display monument of that city.
#                   City                                 Monument
#                   Delhi                               Red Fort
#                   Agra                                Taj Mahal
#                   Jaipur                              Jal Mahal

def city_monument(city):
    if city.upper() == "DELHI":
        print("Red Fort")
    elif city.upper() == "KOLKATA":
        print("Hazarduari")
    elif city.upper() == "AGRA":
        print("Taj Mahal")
    elif city.upper() == "JAIPUR":
        print("Jal Mahal")
    else:
        print("Sorry , we do not have any information of monument of the city")


#city = input("Enter your city: ")
#city_monument(city)

# Write a program to find the lowest number out of two numbers excepted from user.
def lowest_num(n1,n2):
    if n1 >n2 :
        print(n2,"is a lowest number")
    else:
        print(n1,"is a lowest number")
#lowest_num(-12.5,-11)

# Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.

def divisible_by2and3(number):
    if number%2==0 and number%3==0 :
        print("it is divisible by 2 and 3 both")
    else:
        print("this number is not divisible by 2 and 3 both")

#divisible_by2and3(16)



