def DFS(n):
    print(n, end=' ')
    visited[n] = 1
    for a in range(len(mat[n])):
        if mat[n][a] == 1 and visited[a] == 0:
            DFS(a)



N, M = 7, 8
route = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
mat = [[0]*(N+1)for _ in range(N+1)]
for i in range(M):
    mat[route[i*2]][route[i*2+1]] = 1
    mat[route[i*2+1]][route[i*2]] = 1
[print(i, mat[i]) for i in range(N+1)]
visited = [0]*(N+1)
DFS(1)