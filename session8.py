# for x in range(10):
#     for y in range(5):
#         print(x, y)

# x = 1
# while x <= 10:
#     y = 1
#     while y <= 5:
#         print(x, y)
#         y += 1
#     x += 1 
# print("*")

# *
# **
# ***
# ****
# *****
# ******
# ****"***
# print("*"*5)


# n = int(input("Enter a number: "))
# for i in range(1, n + 1):
#     # print("*" * i)
#     stars = ""
#     for j in range(i):
#         stars += "*"
#     print(stars)

# *******
# ******
# *****
# ****
# ***
# **
# *
# n = int(input("Enter a number: "))
# for i in range(n, 0, -1):
#     # print("*" * i)
#     stars = ""
#     for j in range(i):
#         stars += "*"
#     print(stars)

#      *
#     **
#    ***
#   ****
#  *****
# ******
# n = int(input("Enter a number: "))
# for i in range(1, n + 1):
#     # print("*" * i)
#     stars = ""
#     for k in range(n-i):
#         stars += " "
#     for j in range(i):
#         stars += "*"
#     print(stars)

# *******
#   *****
#    ****
#     ***
#      **
#       *
# n = int(input("Enter a number: "))
# for i in range(n, 0, -1):
#     # print("*" * i)
#     stars = ""
#     for k in range(n-i):
#         stars += " "
#     for j in range(i):
#         stars += "*"
#     print(stars)

#     1   2   3   4   5   6   7   8   9
# 1   1
# 2   2
# 3   3   6   9   12  15
# 4
# 5
# 6
# 7
# 8
# 9
# msg = 'hello' + str(10) -> '10'
for i in range(1,10):
    row = ''
    for j in range(1,10):
        row += str(i*j) + '    '
    print(row)