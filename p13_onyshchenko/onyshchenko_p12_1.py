letters = 0
f = open('gadsby.txt','r')
for line in f:
    for char in line:
        if char.isalpha():
            letters += 1
print(f"Gadsby have {letters} letters")
f.close()
mass = {}
print(type(mass))
f = open('gadsby.txt','r')
for line in f:
    for i in line.upper():
        if mass.get(i):
            mass[i] += 1
        else:
            mass[i] = 1
f.close()
mass = {key: value for key, value in mass.items() if key.isalpha()}
mass = sorted(mass.items(), key=lambda x:x[1] ,reverse=True)
mass = dict(mass)
n=0
v = []
for key in mass:
    mass[key] /= letters
    mass[key] *= 100
    mass[key] = round(mass[key],3)


print(mass)
