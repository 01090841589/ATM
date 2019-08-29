dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
import itertools
import copy


def go(A):
    global ans

    B = copy.deepcopy(board)
    for i in range(N):
        down_flag = 0
        for j in range(H):
            if B[j][A[i]] == 1:
                B[j][A[i]] = 0
                break
            elif B[j][A[i]] > 1:
                down_flag = 1
                Q = []
                Q.append((j, A[i], B[j][A[i]]))
                while len(Q):
                    z, c, v = Q.pop(0)
                    B[z][c] = 0
                    for d in range(4):
                        y = z
                        x = c
                        for _ in range(v - 1):
                            y += dy[d]
                            x += dx[d]
                            if 0 <= y < H and 0 <= x < W:
                                if B[y][x] == 1:
                                    B[y][x] = 0
                                elif B[y][x] > 1:
                                    Q.append((y, x, B[y][x]))
                                    B[y][x] = 0

                break
        if down_flag:
            for l in range(W):
                Q = []
                for j in range(H):
                    if B[j][l] > 0:
                        Q.append(B[j][l])
                        B[j][l] = 0
                for j in range(len(Q)):
                    B[H - 1 - j][l] = Q[-j - 1]
    tmp = 0
    for i in range(H):
        for j in range(W):
            if B[i][j] > 0:
                tmp += 1
    if tmp < ans:
        ans = tmp


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    board = []
    for i in range(H):
        board.append(list(map(int, input().split())))

    A = list(itertools.product(list(range(W)), repeat=N))
    ans = H * W
    for i in A:
        go(i)
        if ans == 0:
            break
    print("#{} {}".format(tc, ans))