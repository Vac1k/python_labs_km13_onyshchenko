print('Volodymyr Onyshchenko, home work №6')
table = {
    '1': ('.', ',', '?', '!', ':'),
    '2': ('a', 'b', 'c'),
    '3': ('d', 'e', 'f'),
    '4': ('g', 'h', 'i'),
    '5': ('j', 'k', 'l'),
    '6': ('m', 'n', 'o'),
    '7': ('p', 'q', 'r', 's'),
    '8': ('t', 'u', 'v'),
    '9': ('w', 'x', 'y', 'z'),
    '0': ' '
}

def get_key(value):
    for el_1,el_2 in table.items():
        for j in el_2:
            if j == value:
                return el_1, el_2.index(j)

while True:
    print('Input message: ')
    inpt = str(input())
    print('In nums: ')
    res = ''
    for i in range(len(inpt)):
        key, times = get_key(inpt[i].lower())
        if key is not None:
            res += str(key)*(times+1)
    print(res)
