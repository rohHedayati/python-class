#str_value = '10'
#print(type(str_value))
#int_value = int(str_value)
#print(type(int_value))

#x = float(input('Enter a number 1:'))
#x = int(x)
#y = input('Enter a number 2:')
#y = int(y)
#print(x, '*', y, '=', x * y)


#salary = 1000000
#tax = 10
#tax_price = 100000
#pure_salary = 900000
salary = int(input('Enter salary:'))
tax = float(input('Enter tax(%):'))
tax_price = salary * (tax / 100)
pure_salary = salary - tax_price
print("------------------------------")
print(f'Salary : {salary} Rial')
print(f'Tax : {tax} %')
print(f'Tax price : {tax_price}')
print(f'pure salary : {pure_salary}')
