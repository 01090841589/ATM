T = int(input())
for test_case in range(1, T+1):
    cnt =0
    N = int(input())
    n = list(map(int, input().split()))
    total = 0
    MAX = 0
    for i in range(N):
        total += n[i]
        if total < 0:
            total = 0
        if MAX < total:
            MAX = total
    print(MAX)