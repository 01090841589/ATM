import sys
sys.stdin = open("BFS.txt")
def BFS(v):
    queue = []
    queue.append(v)
    visited[v] = 1
    print(v)
    while len(queue) != 0:
        t = queue.pop(0)
        for i in range(1, N+1):
            if G[t][i] and not visited[i]:
                queue.append(i)
                visited[i] = visited[t]+1
                print(i, end=' ')
                print(visited)
        print()
route = list(map(int, input().split()))
node = []
N = len(route)//2
G = [[0 for _ in range((N+1))] for _ in range(N+1)]
visited = [0]*(N+1)
for i in range(0, len(route), 2):
    G[route[i]][route[i+1]] = 1
    G[route[i+1]][route[i]] = 1
[print(G[i]) for i in range(N)]
BFS(1)