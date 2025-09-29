# f = open("files/test.txt")
# print(f.read(10))
# print(f.readlines())
# for x in f:
#     print(x)
# f.close()

# with open("files/test1.txt","a") as f:
#     f.write("\nhi")
s = 0
c = 0
with open("files/test.txt") as file:
    for number in file:
        s += float(number)
        c += 1

avg = s / c
sum_col = "Sum"
count_col = "Count"
avg_col = "AVG"
print(f"{sum_col:^15}|{count_col:^15}|{avg_col:^15}")
print(f"{s:^15}|{c:^15}|{avg:^15.2f}")