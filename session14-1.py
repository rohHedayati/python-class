students_score_dict = {
    'ali': 15.25,
    'mahdi': 10,
    'mina': 17,
    'sara': 20
}

# print(students_score_dict.items())
# for x,y in students_score_dict.items():
#     print(f"key: {x}, Value: {y}")


number_list = [1,10,15,20,16]
# for i in range(len(number_list)):
#     print(i, number_list[i])

# for i,x in enumerate(number_list):
#     print(i,x)

# for x in number_list:
#     print(x)


# --------------------------------------------------------------------
# Sets
# students_set = {'ali', 'mahdi', 'mina', 'sara'}
# # Adding items
# students_set.add('new_student')  # Add a single item
# students_set.update(['new_student1', 'new_student2'])  # Add multiple items

# students_set.remove('ali')  # Remove an item, raises KeyError if not found
# students_set.discard('mahdi')  # Remove an item, does not raise error if
# # not found
# students_set.pop()  # Remove and return an arbitrary item
# students_set.clear()  # Clear all items
# # Find item
# if 'ali' in students_set:
#     print('ali is in the set')

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# Union
# set_union = set1 | set2  # or set1.union(set2)
# print(set_union)
# Intersection
# set_intersection = set1 & set2  # or set1.intersection(set2)
# print(set_intersection)

# Difference
# set_difference = set1 - set2  # or set1.difference(set2)
# print(set_difference)
# Symmetric Difference
# set_symmetric_difference = set1 ^ set2  # or set1.symmetric_difference(set2)
# print(set_symmetric_difference)
# # Subset and Superset
# is_subset = set1 <= set2  # or set1.issubset(set2)
# is_superset = set1 >= set2  # or set1.issuperset(set2)

# --------------------------------------------------------------------
import random
random_numbers = []

for i in range(20):
    z = random.randint(1,10)
    random_numbers.append(z)

# unique_numbers = []
# for x in random_numbers:
#     if x not in unique_numbers:
#         unique_numbers.append(x)

print(random_numbers)
# print(unique_numbers)
unique_num = list(set(random_numbers))
# unique_num = list(unique_num)
print(unique_num)

# print(sum(random_numbers, 100000))