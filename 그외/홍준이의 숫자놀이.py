def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

T = int(input())
for test_case in range(1, T+1):
    x, y = map(int, input().split())
    a, X, Y = egcd(x, y)
    if a > 0:
        print('#{} {} {}'.format(test_case, X, Y))
    else:
        print('#{} -1'.format(test_case))
