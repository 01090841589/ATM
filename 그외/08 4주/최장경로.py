import sys
sys.stdin = open("최장경로.txt")

def max_route(N, k, cnt):
    if k == 0:
        print(cnt)
    for i in range(N):
        if visited[i] == 1:
            return
        if mat[k][i] == 1:
            visited[i] = 1
            max_route(N, i, cnt+1)
            visited[i] = 0

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    route = [list(map(int, input().split())) for _ in range(M)]
    print(route)
    mat = [[0]*N for _ in range(N)]
    for road in route:
        mat[road[0]-1][road[1]-1] = 1
        mat[road[1]-1][road[0]-1] = 1
    [print(mat[i]) for i in range(N)]
    visited = [[0]*N for _ in range(N)]
    max_route(N, 0, 0)