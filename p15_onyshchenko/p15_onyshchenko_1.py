
def Print_Pascal(rows):
    row = [1]

    for i in range(rows):
        yield row
        row = [sum(i) for i in zip([0]+row, row+[0])]


P = Print_Pascal(99999999999)

num = int(input("Enter:"))
for i in range(num+1):
    print(next(P))
