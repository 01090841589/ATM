import sys
sys.stdin = open("최적경로.txt")
def perm(n ,k):
    global result
    if n == k:
        total = 0
        now = [0,0]
        now[0] = work[0]
        now[1] = work[1]
        # for i in a:
        #     total += abs(now[0]-customer[i-1][0])+abs(now[1]-customer[i-1][1])
        #     now[0] = customer[i-1][0]
        #     now[1] = customer[i-1][1]
        #     if result <= total:
        #         break
        # total += abs(home[0]-customer[i-1][0])+abs(home[1]-customer[i-1][1])
        # if result > total :
        #     result = total
    else:
        for i in range(k, n):
            a[i], a[k] = a[k], a[i]
            perm(n, k+1)
            a[i], a[k] = a[k], a[i]
# def sell()
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = list(map(int, input().split()))
    home = [M[0], M[1]]
    work = [M[2], M[3]]
    customer = [[M[2*i], M[2*i+1]] for i in range(2, len(M)//2)]
    result = 200*N
    a = [i for i in range(1, N+1)]
    perm(N, 0)
    print('#{} {}'.format(tc, result))