# print("Mohsin Zaidi")
# print(' o=========/¬')
# print('  _|_||_|/')
# print('*' * 10)
#
# price=10
# price=20
# print(price)
#

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

print("This is car game ")
comand = ""
while comand !="q"or comand != "Q":
    comand=input ( "\nPress  any key to change function if you need help then press 'H'/'h': " ).lower()
    if comand == "H" or comand == "h":
        print("'ST'/'st'-- to start the car \n'SP'/'sp'-- to stop the car \n 'Q'/'q'-- to quit or exit")
        print("\nNote: If You Press any other  Key this Program not work  ")
    if comand == "ST" or comand == "st":
        print("This Car is Start")
        while comand == "ST" or comand == "st":
            print("This Car is already started")
    if comand == "SP" or comand == "sp":
        print("This Car is Stopped")
    if comand == "Q" or comand == "q":
            print("Game Over")
            break
    else:
        print("\nSorry we don't have this type of command ")


print("This game is exit so if you run this command again then run the program again ")



