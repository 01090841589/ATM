import sys
sys.stdin = open('피자굽기.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    print(data)
    oven = []
    for i in range(N):
        a = data.pop(0)
        if len(oven) < N:
            oven.append(a)

    while True:
        print(oven, data)
        for j in range(N):
            oven[j] //= 2
            if oven[j] < 1 and data:
                oven[j] = data.pop(0)

    print(oven)