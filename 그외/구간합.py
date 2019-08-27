import sys
sys.stdin = open("구간합.txt")
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    total = 0
    for i in range(N, M+1):
        if i < 10:
            total += i
        else:
            while i >= 10 :
                total += i % 10
                i //= 10
            total += i% 10
    print('#{} {}'.format(tc, total))
    total = 0
    k = 1
    while M > 10:
        while N % 10 != 0:
            i = N
            if i < 10:
                total += i
            else:
                while i >= 10 :
                    total += i % 10
                    i //= 10
                total += i% 10
            N += 1
        while M % 10 != 9:
            i = M
            if i < 10:
                total += i
            else:
                while i >= 10 :
                    total += i % 10
                    i //= 10
                total += i% 10
            M -= 1
        print(N, M, k)
        total += (M // 10 - N // 10 + 1) * k * 45
        k *= 10
        N //= 10
        M //= 10
        print(N, M, k)
    print(total)