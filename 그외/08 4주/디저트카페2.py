import sys
sys.stdin = open("디저트카페.txt")
DIR = [[1, -1], [1, 1], [-1, 1], [-1, -1]]
def rectan_search(y, x, left_down, right_down, left_up, right_up,  visited):
    global result, ori_x, ori_y
    if ori_y == y and ori_x == x and visited != '':
        if len(visited) > result:
            result = len(visited)
            print(visited, visit)
            return
    if gone[y][x]:
        return
    if 0 <= x-1 and y+1 < N and right_down == 0:
        if mat[y+1][x-1] not in visited:
            visited.append(mat[y+1][x-1])
            visit.append([y, x])
            gone[y][x] = 1
            rectan_search(y+1, x-1, left_down+1, right_down, left_up, right_up, visited)
    if x+1 < N and y+1 < N and left_down > 0 and left_up == 0:
        if mat[y+1][x+1] not in visited:
            visited.append(mat[y+1][x+1])
            visit.append([y, x])
            gone[y][x] = 1
            rectan_search(y+1, x+1, left_down, right_down+1, left_up, right_up, visited)
    if x+1 < N and 0 <= y-1 and right_down > 0 and right_up == 0:
        if mat[y-1][x+1] not in visited:
            visited.append(mat[y-1][x+1])
            visit.append([y, x])
            gone[y][x] = 1
            rectan_search(y-1, x+1, left_down, right_down, left_up+1, right_up, visited)
    if 0 <= x-1 and 0 <= y-1 and left_up > 0:
        if mat[y-1][x-1] not in visited:
            visited.append(mat[y-1][x-1])
            visit.append([y, x])
            gone[y][x] = 1
            rectan_search(y-1, x-1, left_down, right_down, left_up, right_up+1, visited)
    if len(visit) >1:
        visit.pop()
        visited.pop()
        rectan_search(visit[-1][0], visit[-1][1], left_down, right_down, left_up, right_up, visited)
T = int(input())
for tc in range(1, 5):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for y in range(N-2):
        for x in range(N-1):
            gone = [[0] * N for _ in range(N)]
            visit = []
            ori_y = y
            ori_x = x
            rectan_search(y, x, 0, 0, 0, 0, [])
    if result < 4:
        result = -1
    print('#{} {}'.format(tc, result))