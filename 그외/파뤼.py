T = int(input())
for a in range(T):
    N, M = map(int, input().split(' '))
    fly = [list(map(int, input().split())) for _ in range(N)]
    max_num = 0
    for i in range(N-M+1) :
        for j in range(N-M+1) :
            sum_num = 0
            for l in range(M) :
                for m in range(M) :
                    sum_num += fly[l+i][m+j]
            if max_num < sum_num :
                max_num = sum_num
    print('#{0} {1}'.format(a+1, max_num))