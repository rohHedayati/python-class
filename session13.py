# Sort
user_name_list = ['user10', 'user12', 'aliabadi','User3', 'User4', 'user30']
grade = [10.25,9,10,14.25,17]

# grade.sort()
# print(grade)

# grade.sort(reverse=True)
# print(grade)

# print("HEllo".lower())
# print("HEllo".upper())
# user_name_list.sort(key=str.lower)
# print(user_name_list)

# print(sorted(grade))

# Copy List
# new_grade = grade.copy()
# new_grade = grade[:]
new_grade = list(grade)
new_grade.sort()
# print(new_grade)
# print(grade)
# ======================================================
# Tuples
new_tuple1 = ('ali', 'mahdi', 'mina')
# print(new_tuple1[0])
# new_tuple1[0] = 'Soheil'
# =======================================================
# Dictionaries
students_score_dict = {
    'ali': 15.25,
    'mahdi': 10,
    'mina': 17,
    'sara': 20
}
# print(students_score_dict['mina'])
# print(students_score_dict.get('mahdii', 'Not found'))
print(students_score_dict.keys())
print(students_score_dict.values())
print(students_score_dict.items())

