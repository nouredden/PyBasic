print("hello")
print("world")

x = 4.2
y = 4
print(x**y)
print(round(x**y))

# a = int(input("Please enter First number:"))
# b = int(input("Please enter Second number:"))
# c = a*b
# print(f"the multiplication result is: {c}")

x = str (83)
print (x[0])
print (x[1])
y = int (x)
print (y)
print(chr(y))

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
number = "00111010"
print(int(number, 2))
print(bin(58))
print(hex(58))
print(oct(58))
print("="*45)
number = int(input("Enter you number . ."))
if number % 7 ==0 :
    print("Your number is diviseble by 7 !!")
else:
    print("your number cannot by devided by 7 !!")

print("Program Ended")
