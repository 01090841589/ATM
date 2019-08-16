T = int(input())
for test_case in range(1, T+1):
    D, H, M = map(int, input().split())
    total = (D*24*60)+H*60+M
    now = 11*24*60+11*60+11
    if total-now < 0:
        print('#{} -1'.format(test_case))
    else:
        print('#{} {}'.format(test_case, total-now))