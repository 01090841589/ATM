import sys, copy
sys.stdin = open("보호필름.txt")

def find_source(visited):
    for x in range(W):
        status = []
        cnt = 1
        for y in range(D):
            if y != 0:
                if mat[y][x] == mat[y-1][x]:
                    cnt += 1
                else :
                    cnt = 1
                status.append(cnt)
                if cnt >= K:
                    break
            else:
                status.append(cnt)
        if y == D-1:
            change_source(x, status, visited)
    return
def change_source(x, status, visited):
    global count, result
    buf = []
    cor = max(status)
    if cor < K:
        cnt = 1
        for i in range(D):
            if i != 0:
                if mat[i][x] == mat[i-1][x]:
                    cnt += 1
                else :
                    cnt = 1
            if cnt == cor:
                if i-2 > 0:
                    if visited[i-2] == 0:
                        buf.append([i-2, mat[i-1][x]])
                if i+1 < D:
                    if visited[i+1] == 0:
                        buf.append([i+1, mat[i-1][x]])
        for change in range(len(buf)):
            for X in range(W):
                mat[buf[0][0]][X] = buf[0][1]
                if visited[buf[0][0]] == 0:
                    count += 1
                visited[buf[0][0]] = 1
            find_source(visited)
    if result < count:
        result = count

T = int(input())
for tc in range(1, 11):
    D, W, K = map(int, input().split())
    origin = [list(map(int, input().split())) for _ in range(D)]
    result = 0
    count = 0
    mat = copy.deepcopy(origin)
    find_source([0]*D)
    print(result)

