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

