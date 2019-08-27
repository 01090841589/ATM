import sys
sys.stdin = open("수의새로운연산.txt")
T  = int(input())
for test_case in range(1, T+1):
    dot = list(map(int, input().split()))
    cal_dot = [0, 0]
    for N in dot:
        x, y = 0, 0
        c = 1
        while True:
            if c == N:
                cal_dot[0] += x+1
                cal_dot[1] += y+1
                break
            x += 1
            y -= 1
            c += 1
            if y < 0:
                y = x
                x = 0
    while True:
        if y < 0:
            y = x
            x = 0
        x += 1
        y -= 1
        c += 1
        if cal_dot[0]-1 == x and cal_dot[1]-1 == y:
            print('#{} {}'.format(test_case, c))
            break