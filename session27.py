import json

class Person:
    num_legs = 2
    num_hands = 2

    def __init__(self, n):
        self.name = n
        self.created = True

    def __str__(self):
        return f"Person: {self.name} is created!"

    def speak(self):
        print(f"hello my name is {self.name}")

person1 = Person("Soheil")
print(person1)
# person2 = Person("Yasin")
# person3 = Person("Erfan")
# print(person1.speak())
# print(person2.speak())
# print(person3.speak())

def menu():
    print("Enter 1: To insert information")
    print("Enter 2: To show information")
    print("Enter 0: To exit")
    ch = int(input("Enter your choice:"))
    if ch == 1:
        insert()
    elif ch == 2:
        show()
    elif ch == 0:
        return
    else:
        print("Wrong option!")
    menu()

def insert():
    n = int(input("Enter n:"))
    info = []
    for i in range(n):
        name = input("Enter student name:")
        grade = float(input("Enter student grade:"))
        student_info = {
            "name": name,
            "grade": grade
        }
        info.append(student_info)
    try:
        with open("files/student_info.json", "w") as f:
            json.dump(info, f, indent=4)
    except Exception as e:
        print(f"Can not write! error: {e}")
    else:
        print("Information saved!")

def show():
    heading = "Students Grade List"
    row_col = "Row"
    student_name_col = "Student Name"
    grade_col = "Grade"

    try:
        with open("files/student_info.json") as f:
            info = json.load(f)
    except Exception as e:
        print(f"Can not read! error: {e}")
    else:
        print("="*70)
        print(f"{heading:^70}")
        print("="*70)
        print(f"{row_col:^10}|{student_name_col:^30}|{grade_col:^30}")
        print("-"*70)
        for i,x in enumerate(info):
            print(f"{i+1:^10}|{x['name']:^30}|{x['grade']:^30.2f}")
            print("."*70)
        print("="*70)
# menu()