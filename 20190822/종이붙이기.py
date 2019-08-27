import sys
sys.stdin = open("종이붙이기.txt")
def inf_sec(N, num):
    global total
    if N == 0:
        total += num
    if N >= 10:
        inf_sec(N-10, num)
    if N >= 20:
        inf_sec(N-20, num*2)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    total = 0
    inf_sec(N, 1)
    print('#{} {}'.format(tc, total))