print ('Twinkle, twinkle, little star,')
print ('How I wonder what you are!') 
print('		Up above the world so high,')   		
print('		Like a diamond in the sky.') 
print('Twinkle, twinkle, little star,') 
print('	How I wonder what you are')

import sys
print("Python version")
print(sys.version)
print("version info.")
print(sys.version_info)

import datetime
now = datetime.datetime.now()
print("Current date and time: ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))


from math import pi
r = float(input("Input the radius of the circle : "))
area = pi * r ** 2
print("The area of the circle with radius " + str(r) + " is: " + str(area))


fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print("Hello  " + lname + " " + fname)


values = input("Input some comma-separated numbers: ")
list = values.split(",")
tuple = tuple(list)
print('List : ', list)
print('Tuple : ', tuple)


filename = input("Input the Filename: ")
f_extns = filename.split(".")
print("The extension of the file is : " + repr(f_extns[-1]))


color_list = ["Red", "Green", "White", "Black"]
print("%s %s" % (color_list[0], color_list[-1]))


exam_st_date = (11, 12, 2014)
print("The examination will start from : %i / %i / %i" % exam_st_date)


a = int(input("Input an integer: "))
n1 = int("%s" % a)        
n2 = int("%s%s" % (a, a))   
n3 = int("%s%s%s" % (a, a, a))   
print(n1 + n2 + n3)

print(sorted.__doc__)


import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))


print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")


from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)


pi = 3.1415926535897931
r = 6.0
V = 4.0/3.0 * pi * r**3
print('The volume of the sphere is: ', V)


def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2
print(difference(22))
print(difference(14))


def near_thousand(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))
print(near_thousand(2200))


def sum_thrice(x, y, z):
    sum = x + y + z
    if x == y == z:
        sum = sum * 3
    return sum
print(sum_thrice(1, 2, 3))
print(sum_thrice(3, 3, 3))


def new_string(text):
    if len(text) >= 2 and text[:2] == "Is":
        return text
    else:
        return "Is" + text
print(new_string("Array"))
print(new_string("IsEmpty"))


def larger_string(text, n):
    result = ""
    for i in range(n):
        result = result + text
    return result
print(larger_string('abc', 2))
print(larger_string('.py', 3))

num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")


def list_count_4(nums):
  count = 0
  for num in nums:
    if num == 4:
      count = count + 1
  return count
print(list_count_4([1, 4, 6, 7, 4]))  
print(list_count_4([1, 4, 6, 4, 7, 4]))  


def substring_copy(text, n):
  flen = 2
  if flen > len(text):
    flen = len(text)
  substr = text[:flen]
  result = ""
  for i in range(n):
    result = result + substr
  return result
print(substring_copy('abcdef', 2)) 
print(substring_copy('p', 3)) 


def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(is_vowel('c')) 
print(is_vowel('e')) 


def is_group_member(group_data, n):
    for value in group_data:
        if n == value:
            return True  
    return False  
print(is_group_member([1, 5, 8, 3], 3))  
print(is_group_member([5, 8, 3], -1))    
















