def fact(n):
    f = 1
    for x in range(n,0,-1):
        f *= x
    return f

# print(fact(5))

# 4! = 4*3*2*1
# 4! = 4*3!
# n! = n * n-1 * n-2 * ... * 2 * 1
# n! = n * (n-1)!
def fact_rec(n):
    if n == 1:
        return 1
    return n * fact_rec(n-1)


# 1,1,2,3,5,8,13,21,34
# n=7
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1) + fib(n-2)


# print(fib(12))

# 
def sum_numbers(n):
    if n == 1:
        return 1
    return sum_numbers(n-1)+n

# print(sum_numbers(5))


def pow(x, n):
    if n==1:
        return x
    return x * pow(x, n-1)


# print(pow(2,6))
# print(pow(4,3))

def num_digits(n):
    if n<10:
        return 1
    return num_digits(n//10) + 1

print(num_digits(12456))
