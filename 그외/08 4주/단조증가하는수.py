T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = ''.join(list(map(str, input().split())))
    print(A)
    total = 0
    num = 0
    for i in A:
        if num == 0:
            num = int(i)
        if int(i) > num:
            if int(i)*num > total:
                total = int(i)*num
        num = int(i)
    print('#{} {}'.format(tc, total))