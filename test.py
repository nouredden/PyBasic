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
print("hello world")
mylist = ["nour", "douaa", "zainab", "riyad"]
print(mylist)
mylist.append("tarek")
print(mylist)
name , age , country = "NOUR EDDEN", "29" , "SYRIA"
print(f"Name : {name}\nAge :{age}\nCountry: {country}")
print(f"Hello My name is {name},I am {age} Years Old, and I am from {country}")
print(type(name))
print(type(age))
print(type(country))
print(f"\"Hello \'{name}\', How You Doing \\ \n \"\"\" Your Age Is \"{age}\"\" + \n And Your Country Is: {country}")

name = 'Elzero'
print(f"Second letter is : {name[1]} \n Third letter is : {name[2]} \n Last letter is : {name[-1]}")
print(f" {name[1:4]} \n  {name[0::2]} \n  {name[-2::-2]}")
name = '#@#@Elzero#@#@'
print(name.strip('#@#@'))
num = '9'
print(num.zfill(4))
num = "15"
print(num.zfill(4))
num = "130"
print(num.zfill(4))
num = "950"
print(num.zfill(4))
num = "1500"
print(num.zfill(4))
name_one = 'NOUR'
name_two = 'NOUR_ALREZ'
print(name_one.rjust(20,'@'))
print(name_two.rjust(20,'@'))
name_one = 'Nour_Edden'
name_two = 'NouR_ALrEZ'
print(name_one.swapcase())
print(name_two.swapcase())
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count('Love'))
print(name_one.index('o'))