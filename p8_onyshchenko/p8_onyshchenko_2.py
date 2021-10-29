import math
def _input():
    num = []
    letters = ['a','b','c']
    i=0
    for i in range(3):
        try:
            print("Enter",letters[i],":")
            qu = float(input())
            num.append(qu)
        except ValueError:
            print("Ви ввели не число")
    return num

def D(nums):

    d = nums[0]**2-4*nums[1]*nums[2]
    print("Discriminant is:",d)
    return d

def Exptns(nums , d):
    try:
        x1 = (-nums[1] + math.sqrt(d)) / (2*nums[0])
        x2 = (-nums[1] - math.sqrt(d)) / (2 * nums[0])
        print("x1 is:",x1,"  ","x2 is:",x2)
    except ValueError:
        print("Discriminant is <0")
    except ZeroDivisionError:
        print('Division on zero')

print("The programm can solve tasks like :'a^2*x+b*x+c'")
nums = _input()
Exptns(nums,D(nums))
