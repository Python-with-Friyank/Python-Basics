# Self Practice from https://www.w3resource.com/python-exercises/python-basic-exercises.php
# 1 Write a Python program to print the following string in a specific format (see the output). Go to the editor
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond
# in the sky. Twinkle, twinkle, little star, How I wonder what you are"

# print("""Twinkle, twinkle, little star,
# 	How I wonder what you are!
# 		Up above the world so high,
# 		Like a diamond in the sky.
# Twinkle, twinkle, little star,
# 	How I wonder what you are""")
# print("Twinkle, twinkle, little star, \n \t How I wonder what you are! \n \t\tUp above the world so high, \n \t\t"
#     "Like a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")

# 2 Write a Python program to get the Python version you are using.

# import sys
# print(sys.version)
# import platform
# print(platform.python_version())

# 3 Write a Python program to display the current date and time.

# import datetime
# print("Current date and time :" + str(datetime.date.today()))
# now = datetime.datetime.now()
# print("Current date and time :" + now.strftime("%Y-%m-%d %H:%M:%S"))

# 4. Write a Python program which accepts the radius of a circle from the user and compute the area
#Formula is pi * r * r
#
# from math import pi
# radius = float(input("Enter Radius of a Circle"))
# print("Calculating Area of Circle (pi - "+str(pi)+") with Radius as " + str(radius) + " ....")
# area = pi * radius**2
# print("Area of a Circle with Radius " + str(radius) + " is : " + str(area))

# 5 Write a Python program which accepts the user's first and last name and print
# them in reverse order with a space between them

# firstName = input("Enter your First Name : ")
# lastName = input("Enter your Last Name : ")
# print(lastName  + " " + firstName)

# 6. Write a Python program which accepts a sequence of comma-separated
# numbers from user and generate a list and a tuple with those numbers.

# *** A list is a container which holds comma separated values (items or elements) between square brackets where items
# or elements need not all have the same type. In general, we can define a list as an object that contains multiple
# data items (elements). The contents of a list can be changed during program execution. The size of a list can also
# change during execution, as elements are added or removed from it.
# *** A tuple is container which holds a series of comma separated values (items or elements) between parentheses such
# as an (x, y) co-ordinate. Tuples are like lists, except they are immutable (i.e. you cannot change its content
# once created) and can hold mix data types.

# commaseprated = input("Enter Comma Separated Values : ")
# list = commaseprated.split(',')
# tuple = tuple(list)
# print(list)
# print(tuple)

# 7. Write a Python program to accept a filename from the user and print the extension of that.

# fileName = input("Enter File Name with extension : ")
# print("extension of your file is " + fileName.split('.')[1]) #unsafe
# print("extension of your file is " + fileName.split('.')[-1]) #Safe

# 8 Write a Python program to display the first and last colors from the following list.

# color_list = ["Red","Green","White" ,"Black"]
# print("First Color : " + color_list[0])
# print("Last Color : " + color_list[-1])

# 9  Write a Python program to display the examination schedule. (extract the date from exam_st_date)

# exam_st_date = (11, 12, 2014)
# print("The examination will start from : %s / %s / %s "  %exam_st_date)

# 10 Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn

# n = input("Enter Number : ")
# calculatedn = int(n) + int(n+n) + int(n+n+n)
# print(str(calculatedn))

# 11 Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).

# print(abs.__doc__)

# 12 Write a Python program to print the calendar of a given month and year.

# import calendar as cd
# theyear = int(input("Enter Year "))
# themonth = int(input("Enter Month "))
# print(cd.month(theyear,themonth))


# 13. Write a Python program to print the following here document.

# print("""
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example
# """)

# 14. Write a Python program to calculate number of days between two dates.

# from datetime import date
# from_date = date(2014, 7, 2)
# to_date = date(2014, 7, 11)
# print((to_date - from_date).days)

# 15. Write a Python program to get the volume of a sphere with radius 6.
# formula 4/3 * pi * r*r*r

# r = 6
# from math import pi
# area = 4/3 * pi * r*r*r
# print(area)

# 16. Write a Python program to get the difference between a given number and 17, if the number
# is greater than 17 return double the absolute difference

# def getDiff(n):
#     cons = 17
#     if n <= cons:
#         return   cons - n
#     else:
#         return (n - cons) * 2
# print(getDiff(22))
# print(getDiff(14))

# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000
# def near_thousand(n):
#     return (abs(1000 - n) <= 100) or (abs(2000 - n) <= 100)
#
#
# print(near_thousand(2001))
# print(near_thousand(1000))
# print(near_thousand(2101))
# print(near_thousand(900))
# print(near_thousand(800))
# print(near_thousand(2200))

# 18. Write a Python program to calculate the sum of three given numbers, if the values are equal then
# return three times of their sum

# def calculatesum(value1,value2,value3):
#     sum = value1+ value2 + value3
#     if(value1 == value2 == value3):
#         return sum*3
#     else :
#         return  sum
#
# print(calculatesum(20,20,19))


# 19 Write a Python program to get a new string from a given string where "Is" has been added to
# the front. If the given string already begins with "Is" then return the string unchanged

# inputstr1 = "Is this correct way?"
# inputstr2 = "this is correct way?"
#
# def checkIf(input):
#     lower_string = input.lower()
#     if(len(lower_string) >= 2 and lower_string[:2] == "is"):
#         return input
#     else:
#         return  "Is "+input
#
# print(checkIf(inputstr1))
# print(checkIf(inputstr2))

# 20. Write a Python program to get a string which is n (non-negative integer) copies of a given string.

# number = int(input("Enter Number of Copies needed "))
# string = input("Enter String to Copies ")
#
# if number > 0:
#     print(string * number)


# 21. Write a Python program to find whether a given number (accept from the user) is even or odd, print
# out an appropriate message to the user.

# def checkEvenOdd(number):
#     if number % 2 == 0:
#         return str(number) + " is Even"
#     return  str(number) + " is Odd"
#
# print(checkEvenOdd(2))

# 22 Write a Python program to count the number 4 in a given list.

# list = [1,2,4,4,5,6,3,4,5,4]
# countof4 = 0
# for num in list:
#     if num == 4:
#         countof4 = countof4+ 1
# print(countof4)

# 23. Write a Python program to get the n (non-negative integer) copies of the first 2
# characters of a given string. Return the n copies of the whole string if the length is less than 2

# def printstring(string,number):
#     trimstring = string[:2]
#     print(trimstring*number)
#
# printstring("abc",3)
# printstring("o",3)
# printstring("kjsdc",5)


# 24. Write a Python program to test whether a passed letter is a vowel or not.
# def checkVowel(sentence):
#     list = ['A','E','I','O','U']
#     if str(sentence).upper() in list:
#         return "Its Vowel"
#     return "Its not a Vowel"
#
# print(checkVowel("a"))
# print(checkVowel("A"))
# print(checkVowel("B"))
# print(checkVowel("o"))
# print(checkVowel("Z"))

# 25  Write a Python program to check whether a specified value is contained in a group of values.

# def checkvalueavailable(number,list):
#     if number in list:
#         return print("Its in List")
#     return print("Its not in List")
#
# checkvalueavailable(1,[1,2,3,4,5])
# checkvalueavailable(-1,[1,2,3,4,5])

# 26. Write a Python program to create a histogram from a given list of integers

# list= [1,2,4,5,6,3,2]
# def historgram(list, char):
#     for num in list:
#         print(char * num)
#
# historgram(list,'@')
# historgram(list,'--')
# historgram(list,'+++')


# 27. Write a Python program to concatenate all elements in a list into a string and return it

# def concatinatelistitems(list):
#     strng = ""
#     for item in list:
#         strng = strng + str(item)
#     print(strng)
#
# concatinatelistitems([1,2,3,4,3,'2','a','x'])

# 28. Write a Python program to print all even numbers from a given numbers list in the same order
# and stop the printing if any numbers that come after 237 in the sequence.

# def printeventill237():
#     listtoPrint = []
#     numbers = [
#         386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#         399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#         815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#         958, 743, 527
#     ]
#     for item in numbers:
#         if item % 2 == 0:
#             listtoPrint.append(item)
#         if item == 237:
#             break
#     print(listtoPrint)
#
# printeventill237()

# 29. Write a Python program to print out a set containing all the colors from color_list_
# 1 which are not present in color_list_2.

# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
#
# for item in color_list_1:
#     if item not in color_list_2:
#         print(item)
#
# print(color_list_2.difference(color_list_1))
# print(color_list_1.difference(color_list_2))

# 30. Write a Python program that will accept the base and height of a triangle and compute the area

# def calculateareaoftriangle(base,height):
#     return base * height * 1/2
# print(calculateareaoftriangle(20,40))

# 31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
