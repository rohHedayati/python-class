# number = [1,2,5,3,4]
# zeros = [10]*20
# print(zeros)

# print(number[::-1])
# number.reverse()
# print(number)

# number = [1,2,5,3,4]
# reversed_number = []
# for x in number:
#     reversed_number.insert(0, x)

# print(reversed_number)


# number = [1,2,3,4,5]
# x1 = number[0]
# x2 = number[1]
# x3 = number[2]
# *x1, x2, x3 = number
# print(x1, x2, x3)

grade1 = [10,15,20,15.25,14]
grade2 = [10.25,9,10,14.25,17]
grade = []

# for x in grade1:
#     grade.append(x)
# for y in grade2:
#     grade.append(y)
# print(grade)

# for x in grade1:
#     grade2.append(x)
# print(grade2)

# print(grade1.pop(0))
# print(grade1)
# if 15.75 in grade1:
#     grade1.remove(15.75)
# print(grade1)

# del grade1[1:3]
# print(grade1)

# grade1.clear()
# print(grade1)


# user_name_list = ['aliabadi', 'user1', 'user2', 'user3', 'user4']
# user_name = input("Enter your username:")

# if user_name in user_name_list:
#     idx = user_name_list.index(user_name)
#     print(f"Find in index {idx}")
# else:
#     print("Not found")

import random

numbers = []
for i in range(20):
    x = random.randint(1,10)
    numbers.append(x)
print(numbers)