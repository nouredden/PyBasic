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
sideA = int(input("Enter the SideA length: "))
sideB = int(input("Enter the SideB length: "))
sideC = (sideA**2 + sideB**2)**0.5
print(f"The length of Pythagorean (sideC) is : {sideC}")