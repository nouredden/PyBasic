print("hello")
print("world")

# x = 4.2
# y = 4
# print(x**y)
# print(round(x**y))

# a = int(input("Please enter First number:"))
# b = int(input("Please enter Second number:"))
# c = a*b
# print(f"the multiplication result is: {c}")

# x = str (83)
# print (x[0])
# print (x[1])
# y = int (x)
# print (y)
# print(chr(y))

""" Practice 1.10
Write a short program that computes the length of the
hypotenuse of a right triangle given the two legs as pictured in Fig. 1.23 on
p. 35. The program should use three variables, sideA, sideB, and sideC. The
Pythagorean theorem states that the sum of the squares of the two legs of
the triangle equals the square of the hypotenuse. Be sure to assign all three
variables their correct values and print the length of sideC at the end of the
program. HINT: Raising a value to the 1/2 power is the same thing as finding
the square root. Try values 6 and 8 for sideA and sideB."""
# sideA = int(input("Enter the SideA length: "))
# sideB = int(input("Enter the SideB length: "))
# sideC = (sideA**2 + sideB**2)**0.5
# input("Press any key to continue...")
# print(f"The length of Pythagorean (sideC) is : {sideC}")
# name = input("enter your name Please !!")
# print(f"{name[0]} ASCI Value is : {ord(name[0])}")
# print(f"{name[1]} ASCI Value is : {ord(name[1])}")
# print(f"{name[2]} ASCI Value is : {ord(name[2])}")
# print(f"{name[3]} ASCI Value is : {ord(name[3])}")
# Word = input("enter your Word Please !!")
# print(f"your word capitalized is : {Word.upper()}")

# miles = float(input("Enter the Total number of miles you drove : "))
# tins = float(input("Enter the Total number of tins filled : "))
# price = float(input("enter the price of gas liter .. "))
# mpt = miles/tins
# cost = mpt*1.609/16*price
# print(f"You got {mpt} miles or {mpt*1.609} kilometers on that tank of gas !! \n and a {mpt/16*1.609} kilometers per liter \n cost per kilometer is{cost}")
"""4. Write a program that converts US Dollars to a Foreign Currency. You can do this
by finding the exchange rate on the internet and then prompting for the exchange
rate in your program. When you run the program it should look exactly like this:
What i s the amount of US Dollars you wish to convert? 31.67
What i s the current exchange rate
(1 US Dollar equals what i n the Foreign Currency)? 0.9825
The amount in the Foreign Currency is $31.12"""

# amount = float(input("What i s the amount of US Dollars you wish to convert? "))
# rate = float(input("What i s the current exchange rate \n (1 US Dollar equals what i n the Foreign Currency)?"))
# result = amount*rate
# print(f"The amount in the Foreign Currency is {result}")

"""5. Write a program that converts centimeters to yards, feet, and inches. There are
2.54 cm in an inch. You can solve this problem by doing division, multiplication,
addition, and subtraction. Converting a float to an int at the appropriate time will
help in solving this problem. When you run the program it should look exactly
like this (except possibly for decimal places in the inches):
How many centimeters do you want to convert? 127.25
This i s 1 yards , 1 feet , 2.098425 inches."""
# centimeters = float(input("How many centimeters do you want to convert? "))
# yard = centimeters//91.44
# foot = (centimeters%91.44)//30.48
# inch = ((centimeters%91.44)%30.48)/2.54
# print(f"This is {yard} yards , {foot} feet and {inch} inches .")
# number = "00111010"
# print(int(number, 2))
# print(bin(58))
# print(hex(58))
# print(oct(58))
# print("="*45)
# number = int(input("Enter you number . ."))
# if number % 7 ==0 :
#     print("Your number is diviseble by 7 !!")
# else:
#     print("your number cannot by devided by 7 !!")

# print("Program Ended")

print("="*45)
#Guess and Check
# x = int(input("Enter the First number .. "))
# y = int(input("Enter the Second number .. "))
# z = int(input("Enter the Last number .. "))
# maxNum = x
# if y > maxNum:
#     maxNum = y
# if z > maxNum:
#      maxNum = z
# print(f"{maxNum} is the largest number !!")
"""Practice 2.3 Use the guess and check pattern to determine if a triangle is a
perfect triangle. A perfect triangle has side lengths that are multiples of 3, 4
and 5. Ask the user to enter the shortest, middle, and longest sides of a triangle
and then print “It is a perfect triangle “if it is and “It is not a perfect triangle”
if it isn’t. You may assume that the side lengths are integers. Let your guess be
that the message you will print is “It is a perfect triangle”."""
# shortest =int(input("Enter the shortest side length . ."))
# middle =int(input("Enter the middle side length . ."))
# longest =int(input("Enter the longest side length . ."))
# if (shortest%3 == 0 and middle%4 ==0 and longest%5 ==0):
#     print("It is a perfect triangle")
# else:
#     print("It is not a perfect triangle")

# top = float(input("Enter the nomenator number . ."))
# bottom = float(input("Enter the denomenator number . ."))
# guess = float(input("Enter your Guess . ."))

# result = top / bottom
# biggest = abs(result)
# print(result)
# print(biggest)
# try:
#     top =int(input("Enter your Value . ."))
# except :
#     print("you did not enter a valid number")
#     exit(0)

# try :
#     x = int (input("Please enter an integer:"))
#     y = int (input("Please enter another integer:"))
# except:
#     print("You entered an invalid integer.")
# print("The product of the two integers is",x*y)

"""Write a program that prints a user’s grade given a percent of points achieved in
the class. The program should prompt the user to enter his/her percent of points.
It should then print a letter grade A, A−, B+, B, B−, C+, C, C−, D+, D, D−, F.
The grading scale is given in Fig. 2.11. Use exception handling to check the input
from the user to be sure it is valid. Running the program should look like this:
Please enter your percentage achieved in the class: 92.32
You earned an A- in the class."""
# try:
#     Grade = float(input("Please enter your percentage achieved in the class:"))
# except ValueError:
#     print("Wrong value !!")
# if Grade >= 93.33:
#     print("You earned an A in the class.")
# elif Grade >= 83.33:
#     print("You earned a B in the class.")
# elif Grade >= 73.33:
#     print("You earned a C in the class.")
# elif Grade >= 63.33:
#     print("You earned a D in the class.")
# elif Grade < 60.00:
#     print("You earned an F in the class. You Failed !!")
# sqr=50**0.5
# numb = int(input("Enter your number less than 50!!"))
# print(sqr)
# if numb % 7 == 0 or numb % 6 ==0 or numb % 5 == 0 or numb % 4 ==0 or numb% 3 == 0 or numb % 2 ==0:
#     print(f"{numb} is prime")
# else:
#     print(f"{numb} is not prime")
# dec = oct(numb)
# hec = hex(numb)
# print(dec)
# print(hec)
# print("#"*70)
# print(" Cool Banner ".center(70,"#"))
# print(" written by nour edden alrez ".center(70,"#"))
# print("#"*70)

# Stro = input("Enter your string >> ..").upper()
# for c in Stro :
#     print(c)
# print("\nDone")
# Mylist = []
# shouOsmo =input("please Enter ShouOsmo !!").split()
# for i in range(len(shouOsmo)):
#     Mylist.append(shouOsmo[i])
# Mylist[0] = Mylist[3]
# Mylist[1] = Mylist[4]
# Mylist[4] = Mylist[2]
# Mylist[2] = "I"
# Mylist[3] = "am"
# print(Mylist)

# readUserInput = input("please enter a sequense of integers").split()
# countER = 0
# for a in readUserInput:
#     countER+=1
# print(f"there were {countER} Integers entered")
# numBer = 5
# while numBer != 0:
#     numBer*=numBer-1
# print(numBer)
filename = input("Enter the file name you want to cat ")
catfile = open(filename, "r")
for line in catfile:
    print(line)
catfile.close()
