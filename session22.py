import random
import math

def bin_search(numbers, low, high, x):
    # mid = (low + high) // 2
    if low > high:
        print(f"{x} is not found!")
        return False
    mid = math.floor((low + high) / 2)
    if x == numbers[mid]:
        print(f"{x} is found in index: {mid}")
        return True
    elif x > numbers[mid]:
        return bin_search(numbers, mid+1, high, x)
    else:
        return bin_search(numbers, low, mid-1, x)
    
numbers_list = []
for i in range(10):
    numbers_list.append(random.randint(1,100))
numbers_list.sort()

print(numbers_list)
while True:
    x = int(input("Enter a num:"))
    bin_search(numbers_list, 0, len(numbers_list)-1, x)