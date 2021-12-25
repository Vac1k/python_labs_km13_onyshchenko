import math
def log(base,n):
    if base>0 and base != 1:

        return math.log(n,base)
    else:
        print("Error")


def ln(n):
    if n>0:
        return math.log1p(n)
    else:
        print('error')

def lg(n):
    if n>0:
        return math.log10(n)
    else:
        print('error')

