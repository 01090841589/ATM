import sys
sys.stdin = open("원재의벽꾸미기.txt")
T = int(input())
for test_case in range(1, 1+T):
    MIN = 1000000000
    r, c =0, 0
    N, A, B = list(map(int, input().split()))
    for R in range(int(N**0.5), 0, -1):
        for C in range(N//R-5, N//R+5):
            if R > 0 and C > 0 and R*C <= N:
                if (A * abs(R - C)) + (B * abs(N - R * C)) < MIN:
                    MIN = A * abs(R - C) + B * abs(N - R * C)
                    r = R
                    c = C
    print('#{} {} {} {}'.format(test_case, MIN, r, c))