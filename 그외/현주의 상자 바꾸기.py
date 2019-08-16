# 현주야 상자좀 바꿔라
T = int(input())
for test_case in range(1, T+1):
    N, Q = map(int, input().split())
    box = [0]*N
    print(box)
    num = 1
    for i in range(Q):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            box[j] = num
        num += 1

    print('#{}'.format(test_case),end='')
    for a in range(N):
        print(' {}'.format(box[a]),end='')
    print()