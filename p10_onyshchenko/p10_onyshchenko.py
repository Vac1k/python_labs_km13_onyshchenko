print('Volodymyr Onyshchenko, home work №6')
num = 0

def Quantity_salaries():
    print('Enter how many Salaries you want to calculate')

    while True:
        try:
            qu = int(input())
            if qu >= 1:
                 break
            else:
                 print('You wrote incorrect number')
        except ValueError:
            print("Ви ввели не число")
    print('Enter salary of each employee')
    print('Warning, if you write incorrect salary, the employee wont be added to the list')

    return qu

def Helping():

    n = num + 1
    return n

def Salary_input(x):
    while True:
        salary = []
        for i in range(x):
            try:

                qu = float(input())
                if qu >= 1:
                    salary.append(qu)
                    Helping()
                else:
                    print('You wrote incorrect number')
            except ValueError:
                print("Ви ввели не число")
        break

    print(salary)
    return salary

def Calculations(x):
    _remade_salary = []
    for i in range(len(x)):
        k = x[i] * 1.3
        _remade_salary.append(k)
    return _remade_salary

def apply(x, funk):
    return funk(x)


_inpt_salary = apply(Quantity_salaries(),Salary_input)
remade = apply(_inpt_salary,Calculations)
for k in range(len(_inpt_salary)):
    print('Origin salary:',_inpt_salary[k],'New salary:', round(remade[k] , 3),'Inexation:',round(remade[k]-_inpt_salary[k],3))