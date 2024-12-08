# print("Mohsin Zaidi")
# print(' o=========/¬')
# print('  _|_||_|/')
# print('*' * 10)
#
# price=10
# price=20
# print(price)
# from idlelib.macosx import addOpenEventSupport
# from os import remove
# from typing import List

# rating = 4.9
# is_published = True
# print(is_published)
#
# full_name = 'John Smith'
# age = 20
# is_new = True
#
#
#
#
#
# name = input("Plz Enter your name: ")
# color = input("Plz Enter your Favourite color: ")
#
# print(name + " like "+ color + "Color")
#
#
# birth_year = input("Birth Year: ")
# age = 2024 - int(birth_year)
# print(age)


# birth_year = input("Birth Year: ")
# print(type(birth_year))
# age = 2024 - int(birth_year)
# print(type(age))
# print(age)


# weight_p = input('Plz Enter your weight in lbs: ')
# weight_k =float(weight_p)*0.45359237
# print("weight in kilogram  ",float(weight_k), "kg")

# course = 'He is "genius" Ali is my best Friend I like "donot"'
# print(course[0:-1])
# print("he's saying \"my father is a hero \"")
# first = 'Jhon'
# last = 'Smith'
#
# message = first + ' [' + last +'] is a coder '
# print(message)
#
#
# msg = f'{first * 10} [{last}] is a coder '
# print(msg)

# course = "Arfa Training Session"
# print(course)
# print(course.upper())
# print(course.lower())
# print(course.capitalize())
# print(course)
# print(course.replace("Session","New Session"))
# print(course.find("Session"))
# print('Training' in course)
# print('training' in course)


# #for divide
# print(10/3)
#
# #for removing decimal
# print(10//3)
#
# #for multiply
# print(10*3)
#
# #for power (3 is power of ten )
# print(10**3)
#
# #for remainder(use percentage sign (modulus)
# print(10%3)


# for round the value use round function
# x=3.4
# print(round(x))


#for positive print use abs function
# x=-4
# print(abs(x))


#it is use for function its a library which has builtin math function
# import math


# is_hot = False
# is_cold = False
#
# if is_hot:
#     print("its a hot day ")
#     print("drinks lots of water  ")
#     print("use cap for going  outside ")
# elif is_cold:
#
#      print("its a cold day ")
#      print("wear warm cloth")
#      print("eat dry fruit")
# else:
#
#     print("Enjoy your day ")
#     print("Keep healthy and stay with us ")


# phouse=1000000
#
# is_GoodCredit = True
#
# if is_GoodCredit:
#     print("You have to pay 10%")
#     down_payment = 0.1 *phouse
#     print("which is:$",down_payment)
# else:
#     print("You have to pay 20%")
#     down_payment = 0.2 *phouse
#     print("which is:$",down_payment)

# has_high_income = True
# has_good_credit =False
# has_not_criminal = False
#
#
# if has_high_income or has_good_credit and not has_not_criminal:
#     print("Eligible For Loan ")
# else:
#     print("Not Eligible For Loan ")


#
# temperature=20
#
# if temperature != 30:
#     print("It's a hot day")
# else:
#     print("It's a cold day")
#

# name = input("Enter your name: ")
#
# if len(name) < 3:
#     print("Your name must be longer than 3 characters long")
# elif len(name) > 50:
#     print("Your name must be less then  50 characters long")
# else:
#     print("Names looks good")


#
#
# weight = input("Enter your weight: ")
#
# p_or_k = input("L(b)s or Kg: ")
#
# if p_or_k == "L" or p_or_k == "l":
#     weight = float(weight) / 2.2
#     print("Your weight is ", weight , "kg")
# elif p_or_k == "K" or p_or_k == "k" :
#     weight = float(weight) * 2.2
#     print("Your weight is ", weight , "lbs")
# else:
#     print("Invalid input \n You Have to Enter weight L or K")


# k=1
# while k <= 3:
#   i = int(input( "Guess the number and win the prize:  " ))
#   if i==9:
#       print ( "YOU WON" )
#       break
#   else:
#       print ( "You have ", 3 -k, "more left" )
#       if k < 3:
#           print ( "YOU LOST" )
#       else:
#           print("no worry run the program again")
#       k+=1
#       print ( "TRY AGAIN" )



# h is use help fo declare variable
# h = "help"
# start = "start"
# stop = "stop"

# h=input("Enter 'H'/'h' for help")
# q=input("Enter ' Q '/'q' for Quite"

# print("This is car game ")
# car_started = False  # Tracks whether the car is started
# comand = ""
# while comand !="q"or comand != "Q":
#     comand=input ( "\nPress  any key to change function if you need help then press 'H'/'h'")
#     if comand == "H" or comand == "h":
#         print("'ST'/'st'-- to start the car \n'SP'/'sp'-- to stop the car \n 'Q'/'q'-- to quite")
#         print("\nNote: If You Press any other Key this Program not work  ")
#     elif comand == "ST" or comand == "st":
#         if car_started:
#                 print("The car is already started!")
#         else:
#                 car_started = True
#                 print("The car is now started.")
#     elif comand == "SP" or comand == "sp":
#          if not car_started:
#             print("The car is already stopped!")
#          else:
#             car_started = False
#             print("The car is now stopped.")
#     elif comand == "Q" or comand == "q":
#             print("Game Over")
#             break
#     else:
#         print ( "\nSorry we don't have this type of command " )
#
#
#
# print("This game is exit so if you run this command again then run the program again ")

# i=0
# for item in range(10,50,10):
#     print ( item )
#     i=i+item
#
# print (i)

# this task print "L" shape

# numbers =[1,1,1,1,7]
# for x_count in numbers:
#     output =" "
#     for count in range(x_count):
#         output += "x"
#     print(output)

    # this task print "f" shape
#
# numbers = [8,2,6,2,2]
# for x_counter in numbers:
#     output=' '
#     for count in range(x_counter):
#         output+='x'
#     print(output)





# index=[1,2,3,4,6,7,8,9,]
# i=0
# for largest_index in index:
#     if largest_index < index[i]:
#         largest_index = index[i]
#     else:
#         index[i] = largest_index
# i= i + 1
# print(largest_index)


# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# for row in matrix:
#     print(row)
#     for col in matrix:
#         print ( col )
# matrix[0][1]=20
# print(matrix[:])




# this program remove the repeat value

# numbers=[2,1,3,0,4,5,1,0,4,6,7]
# unique=[]
# for num in numbers:
#     if num not in unique:
#         unique.append(num)
# unique.sort()
# print(unique)



# this program remove the 2 value in the list
# # numbers.remove(2)
# print(numbers)



# # tripple list
# numbers=[1,2,3]
# numbers[{0}:]=10
# print(numbers)
# # print(numbers[0])


# math number into english word
# numbers=input("Please Enter you'r phone number: ")
# numbers_digit={
#     '0':'zero',
#     '1':'one',
#     '2':'two',
#     '3':'three',
#     '4':'four',
#     '5':'five',
#     '6':'six',
#     '7':'seven',
#     '8':'eight',
#     '9':'nine'
# }
# output=" "
# for char in numbers:
#     output += numbers_digit[char] + " "
#
# print(output)


# This is the function for greeting without parameter
# def greet_user():
#     print("Hi Sir/Mam" )
#     print ("Im calling you from The company  ")
#     print("How R U Today ")
#
#
# print("Start")
# greet_user()
# print("Finish")


# This is the function for greeting with parameter
# it gave you error when you don't use parameter when calling

# def greet_user(name):
#
#     print(f"Hi {name}")
#     print ("Im calling you from The company  ")
#     print("How R U Today ")
#
#
#
# greet_user("Jhon")
# greet_user("Alexa")
# print("Finish")



# This is the function for greeting with 2 parameter
# it gave you error when you don't use parameter when calling or using one argument

# def greet_user(First_name,last_name):
#
#     print(f"Hi {First_name} {last_name}" )
#     print ("Im calling you from The company  ")
#     print("How R U Today ")
#
#
#
# greet_user("Jhon","smith")
# greet_user("Alexa","Brian")
# print("Finish")
#
#

# This is the function in which we gave parameter mathematical
# def square(number):
#     return number * number
#
#
# print(square(5))

# In this function we not use return statement in function
# def square(number):
#     print( number * number)
#
# print(square(2))







