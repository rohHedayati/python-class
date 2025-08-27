def is_even_odd(number):
    if number%2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

def is_even_odd_v2(number):
    if number%2 == 0:
        return 'even'
    else:
        return 'odd'

def factorial(n):
    f = 1
    for x in range(1, n+1):
        f *= x
    return f

def add(a, b, c=0):
    return a+b+c

def operation(a, b, op='+'):
    if op == '*':
        return a*b
    elif op == '/':
        return a/b
    elif op == '+':
        return a+b
    elif op == '-':
        return a-b
    else:
        return 0

# print(add(10,5))
# print(operation(10,5,'*'))
# x = int(input("Enter a number:"))
# is_even_odd(x)
# m = is_even_odd_v2(x)
# print(f"{x} is {m} number")

# n = 5
# 5*4*3*2*1
# 1*2*3*4*5
# print(factorial(x))
while True:
    x = float(input("Enter 1st num:"))
    y = float(input("Enter 2nd num:"))
    if x == y == 0:
        break
    op = input("Enter operator (* / + -):")
    res = operation(x, y, op)
    print(f"{x} {op} {y} = {res}")