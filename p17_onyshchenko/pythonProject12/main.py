from logarithm import *
from exp_root import *
from factorial import *

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
while True:
    print("_"*50)
    print(" 1-factorial\n",
          "2-exp2\n",
          "3-exp3\n",
          '4-root2\n',
          "5- root3\n",
          '6-log\n'
          ' 7-ln\n',
          '8-lg')
    print("_"*50)
    try:
        a = int(input("Select funck"))
        print("_" * 50)
        if a>0 and a<9:
            if a == 1:
                try:
                    n = int(input("Enter number:"))
                    print("Factorial = ", fact(n))
                except:
                    print("Enter error")
            if a == 2:
                try:
                    n = float(input("Enter number:"))
                    print("Exp2 = ", exp2(n))
                except:
                    print("Enter error")

            if a == 3:
                try:
                    n = float(input("Enter number:"))
                    print("Exp3=", round(exp3(n),3))
                except:
                    print("Enter error")

            if a == 4:
                try:
                    n = float(input("Enter number:"))
                    if n>0:
                        print("Root2 = ", round(root2(n),3))
                except:
                    print("Enter error")

            if a == 5:
                try:
                    n = float(input("Enter number:"))
                    print("Root3", round(root3(n),3))
                except:
                    print("Enter error")

            if a == 6:
                try:
                    n = int(input("Enter number:"))
                    base = int(input("Enter Base"))
                    if n>0 and base>0 and base!=1:
                        print("Log = ", round(log(base, n),3))
                except:
                    print("Enter error")


            if a == 7:
                try:
                    n = int(input("Enter number:"))
                    if n>0:

                        print("ln = ",round(ln(n),3) )
                except:
                    print("Enter error")


            if a == 8:
                try:
                    n = int(input("Enter number:"))
                    if n>0:

                        print("lg = ", round(lg(n),3))
                except:
                    print("Enter error")
            print("_" * 50)
            e = str(input("Continue? Enter Y or N"))
            print("_" * 50)
            if e.lower() == "y":
                print("_" * 50)
            else:
                print("Game Over")
                break
        else:
            print("Error")
    except:
        print("Error")

