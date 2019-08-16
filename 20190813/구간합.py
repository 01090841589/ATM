import sys
sys.stdin = open("sectionsum.txt")
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    max_sum = 0
    min_sum = 10000*N
    v = list(map(int,input().split()))
    for i in range(N-M+1):
        add = 0
        for j in range(M):
            add += v[i+j]
        if max_sum < add:
            max_sum = add
        if min_sum > add:
            min_sum = add
    print('#{0} {1}'.format(test_case, max_sum-min_sum))