user_name_list = ['aliabadi', 'user1', 'user2', 'user3', 'user4']

user_name = input("Enter your username:")

# if user_name in user_name_list:
#     print("You are ban!")
# else:
#     print("Welcome!")
# idx = -1
# for i in range(len(user_name_list)):
#     if user_name_list[i] == user_name:
#         idx = i
# if idx == -1:
#     print("Not find!")
# else:
#     print(f"Find in index {idx}")


# for i in range(len(user_name_list)):
#     if user_name_list[i] != user_name:
#         continue
#     else:
#         print(f"find in index {i}")



# for i in range(10):
#     if i % 2 == 1:
#         continue
#     print(i)


# ----------------------------------------------------
# Find Max and min
age_list = [10,24,17,16,19,22,16,15]
max_number = 0
min_number = 1000
for x in age_list:
    if x > max_number:
        max_number = x
    if x < min_number:
        min_number = x
print(f"Max number is : {max_number}")
print(f"Min number is : {min_number}")