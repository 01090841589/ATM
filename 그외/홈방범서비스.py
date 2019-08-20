import sys
sys.stdin = open("홈방범.txt")

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    home = []
    result = 1
    for y in range(N):
        for x in range(N):
            if mat[y][x] == 1:
                home.append([y, x])
    for y in range(N):
        for x in range(N):
            dis = []
            for a in range(len(home)):
                dis.append(abs(y-home[a][0])+abs(x-home[a][1]))
            dis.sort(reverse=True)
            for i in dis:
                if (i+1)*(i+1)+i*i <= (len(dis)-dis.index(i))*M and result < len(dis)-dis.index(i):
                    result = len(dis)-dis.index(i)
    print('#{} {}'.format(test_case, result))