def nqueen(lst, N):
    global cnt
    if len(lst) == N: 
        cnt += 1
        return 0
    sch = list(range(N))
    for i in range(len(lst)):
        if lst[i] in sch:
            sch.remove(lst[i]) 
        DIR = len(lst) - i
        if lst[i] + DIR in sch: 
            sch.remove(lst[i] + DIR)
        if lst[i] - DIR in sch:
            sch.remove(lst[i] - DIR)
    if sch != []:
        for i in sch:
            lst.append(i)
            nqueen(lst, N) 
            lst.pop()
    else:
        return 0
T = int(input())
for test_case in range(1, T+1):
    cnt = 0
    num = int(input())
    for i in range(num):
       nqueen([i], num)
    print('#{} {}'.format(test_case, cnt))