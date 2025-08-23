names_list = []
score_list = []
sum_scores = 0

n = int(input("Enter n:"))
for i in range(n):
    name = input("Enter name:")
    score = float(input("Enter score:"))
    sum_scores += score
    names_list.append(name)
    score_list.append(score)
    # print(names_list)
    # print(score_list)

average = sum_scores / n
print('\n')
print('Name \t Score')
print('------------------')
for i in range(len(names_list)):
    print(f'{names_list[i]} \t {score_list[i]}')
print('----------------------')
print(f'Average = {average}')
