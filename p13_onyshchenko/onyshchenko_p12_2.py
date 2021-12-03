f = []
for i in range(1880,2020):
    f.append(f"yob{str(i)}.txt")
print(f)

male = {}
female = {}

for i in f:
    with open(i,"r") as file:
        for line in file:
            if line[1]=="M":
                name_M = name_M+line[0]
            else:
                name_F = name_F + line[0]

#uncomplete