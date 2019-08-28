import sys
sys.stdin = open("사각형.txt")
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    mat = [[0] * M for _ in range(N)]
    ractan = [list(map(int, input().split())) for _ in range(K)]
    darker = dict()
    for i in range(11):
        darker[i] = 0
    total = 0
    for squ in ractan:
        flag = 0
        for y in range(squ[0], squ[2]+1):
            for x in range(squ[1], squ[3]+1):
                if mat[y][x] > squ[4]:
                    flag = 1
                    break
            if flag :
                break
        if flag == 0:
            for y in range(squ[0], squ[2]+1):
                for x in range(squ[1], squ[3]+1):
                        mat[y][x] = squ[4]
    for y in range(N):
        for x in range(M):
            darker[mat[y][x]] += 1
    for i, j in darker.items():
        if total < j:
            total = j
    print('#{} {}'.format(tc, total))