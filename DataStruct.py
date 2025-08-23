number_list = [10,15,20,17,36]
names_list = ['ali', 'mahdi', 'mina']
boolean_list = [True, False, False]
all_list = ['ali', 15, True]
empty_list = []
# print(number_list[2])
# print(type(boolean_list))
# x = list((1,2,3,4,5))

# number_list[4] = 50
# print(number_list)

# number_list.append(100)
# names_list.append('sara')
# all_list.append(17.25)
# empty_list.append(15)

# print(number_list)
# print(names_list)
# print(all_list)
# print(empty_list)

# number_list.insert(0, 200)
# print(number_list)



['ali', 'mina', 'sara']
[15.25, 10, 17]

# name   grade
# ali    15.25
# mina   10
# sara   17

# print(len(number_list))

for i in range(len(number_list)):
    print(number_list[i])

for item in number_list:
    print(item)


# Define list
students = ['ali', 'mahdi', 'mina', 'omid', 'sara']
all_type_list = ['name', 20, 10.25, True]

new_students = list(('Nima', 'saba'))

zeros = [0] * 50

number_list = list(range(50))

len(number_list)


# Access items
students[0]
students[len(students)-1]
students[-1]

students[0:3]
students[:3]
students[1:]
students[-3:-1]

students[1:5:2]
students[::2]
students[::-1]

# Change items
students[0] = 'new name'


# unpacking
nums = [1,2,3,4]
first = nums[0]
second = nums[1]

first, second, third, forth = nums

first, second, *other = nums
first, *middle, last = nums

# Add item
students.append("Rohollah")
students.insert(2, 'ali')

students += ['new person']
students += ['new person1', 'new2']
students += number_list

students.extend(['new1', 'new2'])
students.extend(number_list)


students[2:2] = ['new person1', 'new2']
students[2:3] = ['new person1', 'new2']


# Remove items
students.pop()

students.remove('ali')

del students[2]
del students[2:4]
del students

students.clear()

# Find item
students.index('ali') # -> index or error

if 'ali' in students:
    print(students.index('ali'))

students.count('ali')

for index, name in enumerate(students):
    print(index, name)

# sort
students.sort()  # sorts in place
students.sort(reverse=True)  # sorts in reverse order
students.sort(key=len)  # sorts by length of names
students.sort(key=str.lower)  # sorts case-insensitively
students.sort(key=lambda x: x.lower())  # sorts case-insensitively

for student in sorted(students):
    print(student)

print(sorted(number_list))

# list copy
copy_students = students # creates a reference to the same list

students_copy = students.copy()  # creates a shallow copy
students_copy = students[:]  # another way to create a shallow copy 
students_copy = list(students)  # yet another way to create a shallow copy

# -------------------------------------------------------------------------------------------------
# Tuples
new_tuple1 = ('ali', 'mahdi', 'mina')
new_tuple2 = tuple(('ali', 'mahdi', 'mina')) 

for c in new_tuple1:
    print(c)

# -------------------------------------------------------------------------------------------------
# Dictionaries
students_score_dict = {
    'ali': 15.25,
    'mahdi': 10,
    'mina': 17,
    'sara': 20
}

# Accessing dictionary items
print(students_score_dict['ali'])  # Access by key  
print(students_score_dict.get('ali'))  # Access using get method   
print(students_score_dict.get('unknown', 'Not Found'))  # Default value if key not found
print('ali' in students_score_dict)  # Check if key exists

# Adding items
students_score_dict['new_student'] = 18.5  # Add new key-value pair 
students_score_dict.update({'another_student': 19})  # Update or add multiple items
students_score_dict.update(new_student=16.5)  # Update a single item
students_score_dict['ali'] = 16.75  # Update existing key

# Removing items
students_score_dict.pop('ali')  # Remove by key and return value 
students_score_dict.popitem()  # Remove and return the last inserted key-value pair
del students_score_dict['mahdi']  # Delete by key
students_score_dict.clear()  # Clear all items

# Find item
if 'mahdi' in students_score_dict:
    print(students_score_dict['mahdi'])

# Find item
students_score_dict.keys()  # Get all keys
students_score_dict.values()  # Get all values
students_score_dict.items()  # Get all key-value pairs


# Nested structures
nested_list = [
    ['ali', 15.25],
    ['mahdi', 10],
    ['mina', 17],
    ['sara', 20]
]
students_score_dict = {
    'ali': [15.25, 14.5, 20],
    'mahdi': [10, 12, 15],
    'mina': [17, 18, 19],
}
students_score_dict = {
    'ali': {'math': 15.25, 'science': 14.5, 'english': 20},
    'mahdi': {'math': 10, 'science': 12, 'english': 15},
    'mina': {'math': 17, 'science': 18, 'english': 19},
}

# --------------------------------------------------------------------
# Sets
students_set = {'ali', 'mahdi', 'mina', 'sara'}
# Adding items
students_set.add('new_student')  # Add a single item
students_set.update(['new_student1', 'new_student2'])  # Add multiple items

students_set.remove('ali')  # Remove an item, raises KeyError if not found
students_set.discard('mahdi')  # Remove an item, does not raise error if
# not found
students_set.pop()  # Remove and return an arbitrary item
students_set.clear()  # Clear all items
# Find item
if 'ali' in students_set:
    print('ali is in the set')

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# Union
set_union = set1 | set2  # or set1.union(set2)
# Intersection
set_intersection = set1 & set2  # or set1.intersection(set2)
# Difference
set_difference = set1 - set2  # or set1.difference(set2)
# Symmetric Difference
set_symmetric_difference = set1 ^ set2  # or set1.symmetric_difference(set2)
# Subset and Superset
is_subset = set1 <= set2  # or set1.issubset(set2)
is_superset = set1 >= set2  # or set1.issuperset(set2)