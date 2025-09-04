def is_prime_number(n):
    is_prime = True
    for i in range(2,n):
        if n % i == 0:
            is_prime = False
    return is_prime

def is_prime_number_v2(n):
    count = 0
    is_prime = True
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    if count != 2:
        is_prime = False

    return is_prime


x = int(input("Enter a number:"))
if is_prime_number_v2(x):
    print(f"{x} is a prime number")
else:
    print(f"{x} is not a prime number")