print("Онищенко Володимир Сергiйович" )

def F():
    #блок Введення даних
    name =input("Введiть своє iм'я")
    surname = input("Введiть своє Прiзвище")
    t_num = input("Введiть свiй номер телефон")
    str_name = input("Введiть Назву своєї вулицi ")
    house_n = input("Введiть номер свого будинку")
    flat_n = input("Введiть номер квартири")
    city = input("Введiть своє мiсто")
    index = input("Введiть iндекс")
    country = input("Введiть країну")
    #блок виведення даних
    print(name , surname)
    print(t_num)
    print("Str.",str_name,house_n,"ap.",flat_n,city)
    print(index)
    print(country)
    #блок керування програмою
    print("Ви хочете завершити 'yes', 'no'")
    x = input()
    if x == "yes":
          exit(0)
    elif x == "no":
         return F()

    F()
F()
