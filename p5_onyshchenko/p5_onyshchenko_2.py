print('Volodymyr Onyshchenko, home work №6')
exit = False
while True :


    print('Write down your string')
    print('Each word you should write after space')
    x = input()
    words = x.split()
    n = 0
    m = len(words)-2
    for i in range(len(words)):
        if len(words)== 1:
            continue
        else:
                if n<m:
                    words[i] += ', '
                    n = n + 1
                elif i == len(words)-1:
                    words.insert(len(words) - 1, 'and')
    print(*words)
    exit_variable = input("Якщо ви бажаєте вийти з програми напишiть 'yes': ")
    if exit_variable == "yes":
        break