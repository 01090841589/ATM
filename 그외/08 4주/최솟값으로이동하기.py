import sys
sys.stdin = open('최소이동.txt')

T = int(input())
for tc in range(1, T+1):
    W, H, N = map(int, input().split())
    road = [list(map(int, input().split())) for i in range(N)]
    start = road.pop(0)
    total = 0
    while road:
        arrive = road.pop(0)
        if arrive[1]-start[1] > 0 and arrive[0]-start[0] > 0 :
            K = max(arrive[1]-start[1], arrive[0]-start[0])
            total += K
        elif arrive[1]-start[1] < 0 and arrive[0]-start[0] < 0 :
            K = max(abs(arrive[1]-start[1]), abs(arrive[0]-start[0]))
            total += K
        else:
            total += (abs(arrive[1] - start[1]) + abs(arrive[0] - start[0]))
        start = arrive
        print('#{} {}'.format(tc, total))