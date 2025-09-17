def add(a=0, b=0, c=0):
    return a+b+c

def add2(a,b,*x):
    print(a, type(a))
    print(b, type(b))
    print(x, type(x))
    # return a+b+sum(x)

def pow(numbers):
    print(numbers, type(numbers))
    s = 0
    for x in numbers:
        s += x**2
    return s

# print(pow(1,2,3,4,5))

n = int(input("Enter n:"))
nums = []
for i in range(n):
    x = int(input("Enter number:"))
    nums.append(x)
print(pow(tuple(nums)))


# print(add(10,20,30))
# print(add(10,20))
# print(add(10))
# print(add())
# print(add2(10,20,30,40))
# print(add2(10,20))
# print(add2(10,20,1,2,3,4,56,7,8,5,1,2))