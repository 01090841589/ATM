toner = [2, 4, 3, 5, 4, 6, 5, 3, 1]

for i in range(1):
    group = []
    for j in range(len(toner)//2+1):
        group.append(toner[j])
    toner.append(group)
    group = []
    for k in range(len(toner)//2+1,len(toner)):
        group.append(toner[j])
    toner.append(group)
del toner[0]
print(toner)