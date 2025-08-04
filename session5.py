n = int(input("Enter number of lessons:"))
sum_scores = 0
sum_units = 0

for i in range(n):
    grade = float(input(f"Enter grade of lesson {i+1}:"))
    while grade < 0 or grade > 20:
        print("* Error: 0<= Grade <= 20 *")
        grade = float(input(f"Enter grade of lesson {i+1}:"))
    unit = int(input(f"Enter unit of lesson {i+1}:"))
    while unit < 0:
        print('* Error: Unit > 0*')
        unit = int(input(f"Enter unit of lesson {i+1}:"))
    sum_scores += grade * unit
    sum_units += unit

avg = sum_scores / sum_units
status = ''
if avg < 12:
    status = 'Fail'
elif 12<= avg < 17:
    status = 'Normal'
else:
    status = 'A'

print("=======================================")
print(f"Units = {sum_units}")
print(f"Scores = {sum_scores}")
print(f"Average = {avg}")
print(f"Status = {status}")
print("=======================================")
