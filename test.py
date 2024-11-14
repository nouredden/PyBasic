# this is a comment
"""this is a 
multiple line c
omment but it i
s not working , IDK why.!! """
"""now 
the multi line 
comment 
work
because 
we 
have to write the double qoutations three times at the beggining and the end"""
# print("hello world")
# mylist = ["nour", "douaa", "zainab", "riyad"]
# print(mylist)
# mylist.append("tarek")
# print(mylist)
# name , age , country = "NOUR EDDEN", "29" , "SYRIA"
# print(f"Name : {name}\nAge :{age}\nCountry: {country}")
# print(f"Hello My name is {name},I am {age} Years Old, and I am from {country}")
# print(type(name))
# print(type(age))
# print(type(country))
# print(f"\"Hello \'{name}\', How You Doing \\ \n \"\"\" Your Age Is \"{age}\"\" + \n And Your Country Is: {country}")

# name = 'Elzero'
# print(f"Second letter is : {name[1]} \n Third letter is : {name[2]} \n Last letter is : {name[-1]}")
# print(f" {name[1:4]} \n  {name[0::2]} \n  {name[-2::-2]}")
# name = '#@#@Elzero#@#@'
# print(name.strip('#@#@'))
# num = '9'
# print(num.zfill(4))
# num = "15"
# print(num.zfill(4))
# num = "130"
# print(num.zfill(4))
# num = "950"
# print(num.zfill(4))
# num = "1500"
# print(num.zfill(4))
# name_one = 'NOUR'
# name_two = 'NOUR_ALREZ'
# print(name_one.rjust(20,'@'))
# print(name_two.rjust(20,'@'))
# name_one = 'Nour_Edden'
# name_two = 'NouR_ALrEZ'
# print(name_one.swapcase())
# print(name_two.swapcase())
# msg = "I Love Python And Although Love Elzero Web School"
# print(msg.count('Love'))
# print(name_one.index('o'))
# msg = "I <3 Python And Although <3 Elzero Web School"
# msg2 = msg.replace('<3','Love', 1)
# print(msg2)
# num = 159.650
# mynum = int(num)
# print(mynum)
# print(type(mynum))
# myFriendsList = ['Ali','Shady','Ahmad','Abdullah','Basel']
# print(myFriendsList[0])
# print(myFriendsList[-5])
# print(myFriendsList[4])
# print(myFriendsList[-1])
# print(myFriendsList[0::2])
# print(myFriendsList[1::2])
# myFriendsList[-2::]=['Elzero','Elzero']
# print(myFriendsList)
# myFriendsList.insert(0,'Tarek')
# myFriendsList.append('Ali')
# print(myFriendsList)
# del myFriendsList[0:2]
# print(myFriendsList)
# myFriendsList.pop()
# print(myFriendsList)
# myFriendsList.sort()
# print(myFriendsList)
# myFriendsList.reverse()
# print(myFriendsList)
# print(len(myFriendsList))
# print(myFriendsList.count('Elzero'))
# technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
# for n in technologies[-1]:
#     print(n)

# name = 'nour', 'ali','abdullah'
# print(name[0])
# print(type(name))
# print(len(name))
# nums = (1, 2, 3)
# letters = ("A", "B", "C")
# t3=nums+letters
# print(t3)

# my_tuple = (1, 2, 3, 4)
# a,b,_,d =my_tuple
# print(a)
# print(b)
# print(d)
# my_list = [1, 2, 3, 3, 4, 5, 1]
# myset = set(my_list)
# newlist = list(myset)
# print(newlist)
# print(newlist[0:-1])
# nums = {1, 2, 3}
# letters = {"A", "B", "C"}
# S3 = letters | nums
# print(S3)
# S4 = nums.union(letters)
# print(S4)
# nums.update(letters)
# print(nums)

# my_set = {1, 2, 3}
# print(my_set)
# my_set.clear()
# print(my_set)
# my_set.update('A','B')
# print(my_set)
# my_set.discard('C')
# set_one = {1, 2, 3}
# set_two = {1, 2, 3, 4, 5, 6}
# print(set_one.issubset(set_two))

# print("="*55)
# """Boolians"""
# print(bool("abc"))
# print(bool(123))
# print(bool(["apple", "cherry", "banana"]))
# print(bool(True))
# print(5>3)
# x = 200
# print(isinstance(x, int))
# a = ""
# a1 = ()
# a2 = {}
# a3 = []
# print(bool(a))
# print(bool(a1))
# print(bool(a2))
# print(bool(a3))
# print(bool(False))
# print(bool(0))
# print(bool(""))
# print(bool(None))
# print("="*55)
# HTML = 60
# JS = 60
# CSS = 50
# print(HTML and JS and CSS >= 50)
print("="*55)
# num_one = 10
# num_two = 20
# num = 20
# print(num > num_one or num > num_two)
# print(num > num_one and num > num_two)
# result = num_one+num_two
# print(result)
# print(result**3)
# number2 = result**3%26000
# print(number2)
# print(number2/5)
# print(type(number2/5))
# print(str(number2/5))
# print("="*30)
# name_input = input("Enter your name . .")
# name = str(name_input).strip()
# print(f"HELLO {name.capitalize()} welcome to Python world !!")
# print("="*35)
# age =int(input("Enter Your Age . ."))
# if bool(age <= 16):
#     print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
# else:
#     print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")
firstName = input("Enter your First name . .").strip().capitalize()
secondName = input("Enter your Second name . .").strip().capitalize()
print(f"Hello {firstName} {secondName[0]}. ")
print("="*30)

