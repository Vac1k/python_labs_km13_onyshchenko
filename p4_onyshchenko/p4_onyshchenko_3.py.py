print("Onyshchenko Volodymyr")
def F():
    try:
        #блок введення даних
        wasted_minutes = float(input("Enter how many minutes you spent this month"))
        #основна частина програми
        if wasted_minutes<0:
            print("Please, write correct number")
        elif wasted_minutes<=50:
            print("Your bill for this month is 100 hrivnas")
        elif wasted_minutes>50 and wasted_minutes<=100:
            print("Your bill for this month is 150 hrivnas")
        else:
            if wasted_minutes-100 == int(wasted_minutes-100):
                print("Your bill for this month is :", 150 + int((wasted_minutes - 100)) * 2, "hrivnas")
            else:
                print("Your bill for this month is :", 150 + int((wasted_minutes - 100)+1) * 2, "hrivnas")
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
