def taste(vol, n, choice, scr):
    global max_scr
    if vol > L:
        return
    for i in range(N):
        if max_scr < scr:
            max_scr = scr
        if choice[i] == 1:
            break
        choice[i] = 1
        taste(vol+bag[i][0], n+1, choice, scr+bag[i][1])
        choice[i] = 0
T = int(input())
for test_case in range(1, T+1):
    N, L = map(int, input().split())
    bag = []
    [bag.append(list(map(int,input().split()))) for _ in range(N)]
    callorie = 0
    max_scr = 0
    taste(0, 0, [0]*N, 0)
    print('#{} {}'.format(test_case, max_scr))