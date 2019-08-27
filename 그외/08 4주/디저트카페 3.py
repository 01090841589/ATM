import sys
sys.stdin = open("디저트카페.txt")
DIR = [[1, -1], [1, 1], [-1, 1], [-1, -1]]

def dissert(y, x, ld, rd, lu, ru):
    global result, ori_y, ori_x
    print(visit, visited, y, x, ori_y, ori_x)
    # if ld>0 and rd>0 and lu>0 and ru > 0 and y == ori_y and x == ori_x:
    #     print(visit, visited)
    #     if result < len(visited):
    #         result = len(visited)
    if 0 <= x-1 and y+1 < N and rd == 0:
        if gone[y+1][x-1] :
            return
        if mat[y+1][x-1] not in visited:
            print(y+1, x-1, mat[y+1][x-1], 1)
            visited.append(mat[y + 1][x - 1])
            visit.append([y + 1, x - 1])
            gone[y + 1][x - 1] = 1
            dissert(y + 1, x - 1, ld + 1, rd, lu, ru)
    print(y, x, mat[y][x])
    if x+1 < N and y+1 < N and lu == 0 and ld > 0:
        if gone[y+1][x+1] :
            return
        if mat[y + 1][x + 1] not in visited:
            print(y+1, x+1, mat[y+1][x+1])
            visited.append(mat[y + 1][x + 1])
            visit.append([y + 1, x + 1])
            gone[y + 1][x + 1] = 1
            print(y+1, x+1, mat[y+1][x+1])
            dissert(y + 1, x + 1, ld, rd + 1, lu, ru)
    # if x + 1 < N and y - 1 >= 0 and ru == 0 and rd > 0:
    #     if gone[y-1][x+1] :
    #         return
    #     if mat[y - 1][x + 1] not in visited:
    #         visited.append(mat[y - 1][x + 1])
    #         visit.append([y - 1, x + 1])
    #         gone[y - 1][x + 1] = 1
    #         dissert(y - 1, x + 1, ld, rd, lu + 1, ru)
    # if x - 1 >= 0 and y - 1 >= 0 and lu > 0:
    #     if gone[y-1][x-1] :
    #         return
    #     if mat[y - 1][x - 1] not in visited:
    #         visited.append(mat[y - 1][x - 1])
    #         visit.append([y - 1, x - 1])
    #         gone[y - 1][x - 1] = 1
    #         dissert(y - 1, x - 1, ld, rd, lu, ru + 1)


T = int(input())
for tc in range(1, 5):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for y in range(N-2):
        for x in range(N-1):
            gone = [[0] * N for _ in range(N)]
            visit = []
            visited = []
            ori_y = y
            ori_x = x
            dissert(y, x, 0, 0, 0, 0)
    if result < 4:
        result = -1
    print('#{} {}'.format(tc, result))