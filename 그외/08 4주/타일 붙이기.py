import sys
sys.stdin = open("타일붙이기.txt")

def inf_sec(N, num):
    global total
    if N == 0:
        total += num
        return
    if N >= 1:
        inf_sec(N-1, num)
    if N >= 2:
        inf_sec(N-2, num*2)
    if N >= 3:
        inf_sec(N-3, num)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    total = 0
    inf_sec(N, 1)
    print('#{} {}'.format(tc, total))