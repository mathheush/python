#1
# birth_year = input("What year were you born?: ")
# birth_year = int(birth_year)
# current_year = 2023
# age = current_year - birth_year
# print(f"You are {age} years old.")

#2
# username = input("Enter Your username: ")
# password = input("Enter your password: ")
# secret = len(password) * "*"
# password_length = len(password)
# print(f"{username}, your password {secret} is {password_length} letters long.")

#3
# is_magican = False
# is_expert = True

# check if magican and expert: "you are master magican"

# check if magican but no expert: "at least you are getting there"

# check if you are not magican: "you need magic powers"

# if is_magican and is_expert:
#     print("you are master magican")
# elif is_magican and not is_expert:
#     print("at least you are getting there")
# else: print("you need magic powers")

#4
# my_list = [1,2,3,4,5,6,7,8,9,10]
# total = 0

# for number in my_list:
#     total = total + number
# print(total)

#5
# picture = [
#     [0,0,0,1,0,0,0],
#     [0,0,1,1,1,0,0],
#     [0,1,1,1,1,1,0],
#     [1,1,1,1,1,1,1],
#     [0,0,0,1,0,0,0],
#     [0,0,0,1,0,0,0]
# ]
# def show_tree():
#     fill = "*"
#     empty = " "
#     for row in picture:
#         for pixel in row:
#             if (pixel):
#                 print(fill, end="")
#             else:
#                 print(empty, end="")
#         print("")

# show_tree()
# show_tree()

#6
# some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]
# set_no_duplicates = set(some_list)
# for _ in set_no_duplicates:
#     if _ in some_list:
#         some_list.remove(_)
# print(some_list)

#7
# def checkDriverAge(age=0):

#     age = input("What is your age?: ")

#     if int(age) < 18:
#         print("Sorry, you are too young to drive this car. Powering off")
#     elif int(age) > 18:
#         print("Powering On. Enjoy the ride!");
#     elif int(age) == 18:
#         print("Congratulations on your first year of driving. Enjoy the ride!")
# checkDriverAge()

