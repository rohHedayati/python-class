class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_info(self):
        return f"My name is {self.name}. I'm {self.age} years old."
    
class Teacher(User):
    def __init__(self, name, age, degree, salary):
        super().__init__(name, age)
        self.degree = degree
        self.salary = salary
    
    def show_info(self):
        return f"{super().show_info()} Degree:{self.degree}, Salary:{self.salary}"

class Student(User):
    pass


teacher = Teacher('Hedayati', 30, 'Arshad', 25)
print(teacher.show_info())