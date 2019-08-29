import sys
sys.stdin = open('미로.txt')
DIR = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def bfs_mage(y, x, cnt):
    global result, N
    for c in DIR:
        Y = y + c[0]
        X = x + c[1]
        if 0 <= Y < N and 0 <= X < N:
            if mage[Y][X] == 0:
                mage[Y][X] = 9
                stack.append([Y, X, cnt])
            elif mage[Y][X] == 3:
                # print(cnt)
                result = cnt
                return


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    mage = [list(map(int, input())) for _ in range(N)]
    # [print(mage[i]) for i in range(N)]
    result = 0
    stack = []
    for y in range(N):
        for x in range(N):
            if mage[y][x] == 2:
                stack.append([y, x, -1])
    while stack:
        A = stack.pop(0)
        bfs_mage(A[0], A[1], A[2]+1)
    print('#{} {}'.format(test_case, result))
