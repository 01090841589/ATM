import sys
sys.stdin = open("우뚝선산.txt")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    load = list(map(int, input().split()))
    go_up = 0
    total = 0
    now = 0
    while True:
        go_up = 0
        for i in range(now, len(load)-1):
            if load[i+1] > load[i]:
                if go_up == 0:
                    continue
                else:
                    go_up = 0
                    break
            else:
                if go_up == 0:
                    if now != i:
                        go_up = 1
                        total += 1
                    else:
                        go_up=0
                        break
                else:
                    total += 1
                    continue
        now += 1
        if now >= N-1:
            break
    print('#{} {}'.format(test_case,total))