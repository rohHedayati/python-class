def menu():
    print("Enter 1: Add numbers")
    print("Enter 2: Show results")
    print("Enter 0: To exit")
    ch = int(input("Enter your choice:"))
    file_name = input("Enter file name(.txt):")
    if ch == 1:
        add_numbers(file_name)
    elif ch == 2:
        show_result(file_name)
    elif ch == 0:
        return
    else:
        print("Wrong choice!")
    menu()

def add_numbers(file_name):
    # file_name = input("Enter file name(.txt):")
    n = int(input("Enter n:"))
    with open(f"files/{file_name}.txt",'w') as file:
        for i in range(n):
            x = input("Enter your number:")
            file.write(x+'\n')

def show_result(file_name):
    s = 0
    c = 0
    # file_name = input("Enter file name(.txt):")
    with open("files/"+ file_name +".txt") as file:
        for number in file:
            s += float(number)
            c += 1

    avg = s / c
    sum_col = "Sum"
    count_col = "Count"
    avg_col = "AVG"
    print(f"{sum_col:^15}|{count_col:^15}|{avg_col:^15}")
    print(f"{s:^15}|{c:^15}|{avg:^15.2f}")

# menu()


# Json
import json
# x = '{"name": "Hedayati","age": 30}'
# y = json.loads(x)
# print(x)
# print(type(y))

# z = json.dumps(y, indent=2)
# print(z)

# x = {"name": "Hedayati","age": 30}
# with open("files/data.json", "w") as file:
#     json.dump(x, file, indent=4)

with open("files/data.json") as file:
    data = json.load(file)
print(data)
print(type(data))