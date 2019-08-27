T = int(input())
for test_case in range(1, T+1):
    cnt =0
    N, K = map(int,input().split())
    n = list(map(int, input().split()))
    for i in range(1, 1 << N):
        sums = 0
        for j in range(12):
            if i & (1 << j):
                sums += n[j]
                if sums > K:
                    break
        if sums == K:
            cnt += 1
    print('#{0} {1}'.format(test_case,cnt))