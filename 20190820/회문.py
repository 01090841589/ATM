import sys
sys.stdin = open("회문.txt")
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int,input().split())
    mat = [list(input()) for _ in range(N)]
    word = ''
    for y in range(N):
        for x in range(N-M+1):
            for a in range(M//2):
                if mat[y][x+a] != mat[y][x+M-1-a]:
                    break
                if a == (M//2-1):
                    for i in range(M):
                        word += mat[y][x+i]
    for x in range(N):
        for y in range(N-M+1):
            for a in range(M//2):
                if mat[y+a][x] != mat[y+M-1-a][x]:
                    break
                if a == (M//2-1):
                    for i in range(M):
                        word += mat[y+i][x]
    print('#{} {}'.format(test_case, word))