import sys
sys.stdin = open("해피박스.txt")

def select_box(boxsize, cnt, val):
    global result, N, M
    if boxsize > N:
        return
    if M == cnt:
        if result < val:
            result = val
        return
    if boxsize+box[cnt][0] > N:
        if result < val:
            result = val
    select_box(boxsize+box[cnt][0], cnt+1, val + box[cnt][1])
    select_box(boxsize, cnt+1, val)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(M)]
    visited = [0]*M
    result = 0
    select_box(0, 0, 0)
    print('#{} {}'.format(tc, result))