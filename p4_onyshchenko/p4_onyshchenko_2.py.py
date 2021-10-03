print("Onyshchenko Volodymyr")
def F():
    try:
        #блок введення даних
        scale = float(input("Enter the magnitude of the earthshake by Rihter scale"))
        #основна частина програми
        if scale<2 and scale>0:
            print("The earthshake is Micro")
        elif scale>=2 and scale<3:
            print("The earthshake is Very Minor")
        elif scale >= 3 and scale < 4:
             print("The earthshake is Minor")
        elif scale >= 4 and scale < 5:
            print("The earthshake is Light")
        elif scale >= 5 and scale < 6:
             print("The earthshake is Moderate")
        elif scale >= 6 and scale < 7:
            print("The earthshake is Strong")
        elif scale >= 7 and scale < 8:
             print("The earthshake is Major")
        elif scale>=8 and scale<10:
            print("The earthshake is Great")
        elif scale>=10:
            print("The earthshake is Meteoric")
        else:
            print("You wrote wrong number")
        #блок який вiдповiдає за рекурсивнiсть програми
        print("Ви хочете завершити 'yes', 'no'")
        x = input()
        if x == "yes":
              exit(0)
        elif x == "no":
             return F()
    except ValueError:
        print("Ви ввели не число")
    F()
F()