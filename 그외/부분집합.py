arr = list(map(int,input().split()))
n = len(arr)

for i in range(1, 1<<n):
    sums = 0
    part = []
    for j in range(n):
        if i&(1<<j):
            sums += arr[j]
            part.append(arr[j])
    if sums == 0:
        print(part)
