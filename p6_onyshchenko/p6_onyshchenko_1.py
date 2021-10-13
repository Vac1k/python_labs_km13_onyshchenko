print('Volodymyr Onyshchenko, home work №6')
exit = False
i = 0

def inpt():
    if i == 0:
        print('Write down your first string')
        print('Each word you should write after space')
    else:
        print('Write down your second string')
        print('Each word you should write after space')
    x = input()
    x = x.upper()

    return x

#def delete_space(arr):
    #list_ = []
    #for i in range(len(arr)):
       #if arr[i]==' ':
            #continue
       # else:
            #list_.append(arr[i])
    #return list_

def Check_is_possible(s_1,s_2):
    if s_1|s_2==s_1:
        return 1
    else:
        return 0

def del_(s_):
    if ' ' in s_:
        s_ = s_.remove(' ')
    return  s_


while True:
    frst = set(inpt())
    del_(frst)
    i = i+1
    scnd = set(inpt())
    del_(scnd)
    if Check_is_possible(frst,scnd):
        print("You can make another string")
        print(frst)
        print(scnd)
        i=0
    else:
        print("You can't make another string")
        print(frst)
        print(scnd)
        i=0
    exit_variable = input("Якщо ви бажаєте вийти з програми напишiть 'yes': ")
    if exit_variable == "yes":
        break