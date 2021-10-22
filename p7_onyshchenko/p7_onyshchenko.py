def input_num():
    while True:
        try:
            x = int(input('Enter num'))
            if x < 255 and x > 0:
                return x
            else:
                print('Num is incorrect')
        except ValueError:
            print('Wrong number')

def to_16x():
    num = input_num()
    l_1 = list()
    x = num
    while num > 0:
        end = num % 16
        if end >= 10:
            l_1.append(list_alpha[end - 10])
        else:
            l_1.append(str(end))
        num = num // 16
    if len(l_1) != 2 and x != 0:
        l_1.append('0')
    elif len(l_1) != 2 and x == 0:
        l_1.append('0' * 2)
    l_1.reverse()
    str_def = ''.join(l_1)
    return str_def
while True:
    list_alpha = ('A', 'B', 'C', 'D', 'E', 'F')
    r = to_16x()
    g = to_16x()
    b = to_16x()
    print(r , g , b)

    x = input('If you want to exit write yes')
    if x == "yes":
        break