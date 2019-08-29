import sys
sys.stdin = open('노드의거리.txt')

def BFS(v):
    queue = []
    queue.append(v)
    visited[v] = 1
    while len(queue) != 0:
        t = queue.pop(0)
        for i in range(1, N+1):
            if G[t][i] and not visited[i]:
                queue.append(i)
                visited[i] = visited[t]+1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    route = []
    [route.extend(list(map(int, input().split()))) for _ in range(M)]
    s, g = map(int, input().split())
    node = []
    G = [[0 for _ in range(N+1)] for _ in range(N+1)]
    visited = [0]*(N+1)
    for i in range(0, len(route), 2):
        G[route[i]][route[i+1]] = 1
        G[route[i+1]][route[i]] = 1
    BFS(s)
    if visited[g] > 0:
        print('#{} {}'.format(tc, visited[g]-1))
    else:
        print('#{} {}'.format(tc, visited[g]))