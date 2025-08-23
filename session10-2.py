names_list = []
score_list = []
unit_list = []
sum_scores = 0
sum_units = 0

n = int(input("Enter n:"))
for i in range(n):
    name = input("Enter lesson name:")
    score = float(input("Enter score:"))
    unit = int(input("Enter lesson unit:"))
    
    sum_scores += score * unit
    sum_units += unit

    names_list.append(name)
    score_list.append(score)
    unit_list.append(unit)

average = sum_scores / sum_units
print('\n')
print('Name \t Unit \t Score')
print('------------------------------------')
for i in range(len(names_list)):
    print(f'{names_list[i]} \t {unit_list[i]} \t {score_list[i]}')
print('------------------------------------')
print(f'Average = {average}')
