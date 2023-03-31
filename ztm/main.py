# print("Mateusz Konopka")
# name = input("What is your name?")
# print("Hi " + name)
#
#  Fundamental Data Types
# int
# float
# complex
# -operators:
# +
# -
# *
# **
# /
# //
# %
#
# bool
# str
# list
# tuple
# set
# dict
#
#  Classes -> custom types
#
#  Specialized Data Types
#
# None
#
# Math Functions
# print(round(3.1))
# print(round(3.5))
# print(abs(-3))

#  Operator Precedence
# print(2 + 5 * 3)
# ()
# **
# * /
# + -

# print(bin(78))
# print(int("0b101", 2))

# user_iq = 190
# user_age = user_iq / 4
# print(user_iq)
# print(user_age)

#  Constants
# PI = 3.14
# a,b,c = 1,2,3
# print(a,c,b)
# a += 3
# print(a)

#  KEYWORDS
# and	A logical operator
# as	To create an alias
# assert	For debugging
# break	To break out of a loop
# class	To define a class
# continue	To continue to the next iteration of a loop
# def	To define a function
# del	To delete an object
# elif	Used in conditional statements, same as else if
# else	Used in conditional statements
# except	Used with exceptions, what to do when an exception occurs
# False	Boolean value, result of comparison operations
# finally	Used with exceptions, a block of code that will be executed no matter if there is an exception or not
# for	To create a for loop
# from	To import specific parts of a module
# global	To declare a global variable
# if	To make a conditional statement
# import	To import a module
# in	To check if a value is present in a list, tuple, etc.
# is	To test if two variables are equal
# lambda	To create an anonymous function
# None	Represents a null value
# nonlocal	To declare a non-local variable
# not	A logical operator
# or	A logical operator
# pass	A null statement, a statement that will do nothing
# raise	To raise an exception
# return	To exit a function and return a value
# True	Boolean value, result of comparison operations
# try	To make a try...except statement
# while	To create a while loop
# with	Used to simplify exception handling
# yield	To end a function, returns a generator

# username = "Mateusz"
# password = "Konopka"
# very_long_string = '''
#    /\
#   /  \
#  /    \
# /______\
# '''
# print(very_long_string)
#
# full_name = username + " " + password
# print(full_name)
#
# print(type(int(str(100))))

# Escape Sequence
# weather = "\t It's \"kind of\" sunny \n Hope You'll have a good day!"
# print(weather)

# Formatted Strings
# name = "Johnny"
# age = 55
# print("Hi " + name +". You are " + str(age) + " years old.")
# print(f"Hi {name}. You are {age} years old.")
# print("Hi {}. You are {} years old.".format(name, age))
# print("Hi {1}. You are {0} years old.".format(name, age))

# String Indexes
# selfish = "01234567"
#          # 01234567
# print(selfish[0])
# print(selfish[7])
# [start:stop:stepover]
# print(selfish[0:8:2])
# print(selfish[1:])
# print(selfish[:5])
# print(selfish[-1:])
# print(selfish[::-1])

# Build in Functions
# str()
# int()
# float()
# type()
# print()
# len()
# print(len("Hellllllllllo"))
# greet = "Hellllllo Mateusz"
# print(greet[0:len(greet)])

# quote = "to be or not to be"
# print(quote.upper())
# print(quote.capitalize())
# print(quote.find("be"))
# print(quote.replace("be", "me"))
# quote2 = quote.replace("to", "or")
# print(quote2)
# print(quote)

# Booleans
# bool
# True or False
#
# name = "Mateusz"
# is_cool = False

# is_cool = True
# print(bool(1))
# print(bool(0))

# Type Conversion
# name = "Mateusz Konopka"
# age = 19
# status = "online"
#
# status = "offline"
#
# print(status)

# Lists
# list = [1, 2, 3, 4, 5]
# list1 = ["a", "b", "c"]
# list2 = [1 , "a", True]
# amazon_cart = ["notebooks",
#                "sunglasses",
#                "toys",
#                "grapes"
#                ]
# print(amazon_cart)
#
# # List Slicing
# amazon_cart[0] = "laptop"
# new_amazon_cart = amazon_cart[:]
# new_amazon_cart[0] = "gum"
# print(amazon_cart[0::2])
# print(new_amazon_cart)
# print(amazon_cart)

# Matrix
# matrix = [
#     [1,0,1],
#     [0,1,0],
#     [1,0,1]
# ]
# print(matrix[2][1])

# basket = [1, 2, 3, 4, 5]
# print(len(basket))
#
# # adding
# basket.append(100)
# new_basket = basket
# print(new_basket)
#
# new_list = basket.extend([6])
# print(basket)
#
# # removing
#
# basket.remove(100)
# print(basket)
# basket.pop()
# basket.pop(0)
# print(basket)
# basket.clear()
# print(basket)

# basket = ["a", "x", "b", "c", "d", "e", "d"]
# print(basket.index("d", 0, 5))
# print("d" in basket)
# print("x" in basket)
# print("i" in "Hi my name in Ian")
# print(basket.count("d"))
# print(sorted(basket))
# print(basket)
# basket.sort()
# basket.reverse()
# print(basket)
# print(basket[::-1])
#
# print(list(range(1, 100)))
#
#
# new_sentence = " ".join(["Hi", "my", "name", "is", "Mateusz"])
# print(new_sentence)
#
# #list unpacking
# a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(c)
# print(b)
# print(a)
# print(other)
# print(d)

# weapons = None
# print(weapons)

# Dictionary
# dictionary = {
#     "a": [1,2,3],
#     "b": "Hello",
#     "x": True
# }
# my_list = [{
#     "a": [1,2,3],
#     "b": "Hello",
#     "x": True
# },
#     {
#         "a": [4, 5, 6],
#         "b": "Hello",
#         "x": True
#     }
# ]
# print(dictionary["a"][1])
# print(my_list[1]["a"][1])

# user = {
#     "name": "Mateusz",
#     "weapons": "AK",
#     "age": "19"
# }
# user2 = dict(name = "Szymon")
# print(user.get("age", "No age found"))
# print(user2)
#
# print("age" in user)
# print("Mateusz" in user.keys())
# print("Mateusz" in user.values())
# print(user.items())
# user3 = user.copy()
# user.clear()
# print(user3)
# print(user)
# print(user3.pop("age"))
# user3.popitem()
# user3.update({"name": "Oliwier"})
# print(user3)
# user3.update(names = "Olek")
# print(user3)

# Tuples
# my_tuple = (1,2,3,4)
# print(my_tuple[1])
# print(2 in my_tuple)
#
# user = {
#     (1,2,3): "Mateusz",
#     "weapons": "AK",
#     "age": "19"
# }
# print(user.items())
# print(user[(1,2,3)])
#
# my_tuple = (1,2,3,4,5,5,5,5)
# new_tuple = my_tuple[0:3]
# print(new_tuple)
#
# a,b,c, *other = (1,2,3,4,5)
# print(other)
# print(my_tuple.count(5))
# print(len(my_tuple))
# print(my_tuple.index(2))

# Set

# my_set = {1,2,3,4,5,5}
# my_set.add(100)
# my_set.add(2)
# print(my_set)
# print(1 in my_set)
# print(len(my_set))
# new_set = my_set.copy()
# print(new_set)
#
# my_list = [1,2,3,4,5,5]
# set(my_list)
# list(my_list)
# print(my_list)

# my_set = {1,2,3,4,5}
# your_set = {4,5,6,7,8,9,10}
#
# print(my_set.difference(your_set))
# # my_set.discard(5)
# # print(my_set)
# # my_set.difference_update(your_set)
# # print(my_set)
# print(my_set.intersection(your_set))
# print(my_set.isdisjoint(your_set))
# print(my_set.union(your_set))

# my_set = {4,5}
# your_set = {4,5,6,7,8,9,10}
# print(my_set.issubset(your_set))
# print(your_set.issuperset(my_set))
