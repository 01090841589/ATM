import sys
sys.stdin = open('contact.txt')

def BFS(v):
    queue = []
    queue.append(v)
    visited[v] = 1
    while len(queue) != 0:
        t = queue.pop(0)
        for i in range(1, N+1):
            if G[t][i] and not visited[i]:
                queue.append(i)
                visited[i] = visited[t] + 1


for tc in range(1, 11):
    K, M = map(int, input().split())
    route = list(map(int, input().split()))
    N = max(route)+1
    node = []
    G = [[0 for _ in range(N+1)] for _ in range(N+1)]
    visited = [0]*(N+1)
    for i in range(0, len(route), 2):
        G[route[i]][route[i+1]] = 1
    BFS(M)
    for i in range(N-1, -1, -1):
        if visited[i] == max(visited):
            print('#{} {}'.format(tc, i))
            break