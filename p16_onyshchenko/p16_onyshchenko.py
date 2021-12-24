from functools import wraps
def register(a = True):
    def f_decorator(funck):
        @wraps(funck)
        def wrapper(*args,**kwargs):

            '''wrapper'''
            if a:
                new_book = []
                for i in funck(*args,**kwargs):
                    new_workbook = []
                    for j in range(0, len(i), 4):
                        new_workbook.append(i[j:j + 4])
                    new_book.append(new_workbook)



                return(new_book)
            else:
                return(funck(*args,**kwargs))

        return wrapper
    return f_decorator
@register(a = False)
def first_book(quan ,np):
    '''first book'''
    t = []
    for i in range(1, np+1):
        t.append(i)
    book = []

    for j in range(quan//np):
        t1 = []
        for i in range(len(t) // 2):
            if i % 2 == 0:
                t1.append(t[len(t) - 1 - i] + np * j)
                t1.append(t[0 + i] + np * j)
            else:
                t1.append(t[0 + i] + np * j)
                t1.append(t[len(t) - 1 - i] + np * j)
        #book.append(t1)
        yield t1

    #return book

n = 0
amount_pages = 16
while True:

    n = int(input("enter amount of pages"))
    if n%amount_pages == 0 and n<=1280:
        break



#first_book = register(True)(first_book)

for i in first_book(n,amount_pages):
    for j in i:
        try:
            for k in j:
                print(k, end=",")
            print()
        except TypeError:
            print(j, end=",")
    print()
print("Amount workbook", n//amount_pages)
