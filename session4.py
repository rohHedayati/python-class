# print(1)
# print(2)
# print(3)
# print(4)

# for x in range(10):
#     y = x ** 2
#     print(x)

# while

# start = int(input("Enter start value:"))
# stop = int(input("Enter stop value:"))

# for x in range(start, stop+1):
#     if x % 2 == 1:
#         print(x)

# if start % 2 == 0:
#     start_odd = start + 1
# else:
#     start_odd = start
# for x in range(start_odd, stop+1, 2):
#     print(x)



# for x in range(10):
#     print(x)


# x = 0
# while x < 10:
    # print(x)
    # x = x + 1

# x = 99
# while x >= 1:
#     print(x)
#     x -= 2 


# for x in range(99, 0, -2):
#     print(x)

# n = 5
# sum = 0
# 2  -> sum = 2 
# 3 -> sum = 5
# 5 -> sum = 10
# 4 -> sum = 14
# 8 -> sum = 22

number = int(input("Enter your number:"))
sum = 0
sum_odd = 0
sum_even = 0
for x in range(number):
    y = float(input(f"Enter number {x + 1}:"))
    if y % 2 == 0:
        sum_even += y
    else:
        sum_odd += y
    sum += y  # sum = sum + y
avg = sum / number
print(f"Sum = {sum}")
print(f"AVG = {avg}")
print(f"Sum Even = {sum_even}")
print(f"Sum Odd = {sum_odd}")