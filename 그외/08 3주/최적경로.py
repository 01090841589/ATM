import sys
sys.stdin = open("최적경로.txt")
def sell(now, visit, total, n):
    global result
    if result <= total:
        return
    if n >= N:
        total += abs(now[0]-home[0])+abs(now[1]-home[1])
        result = min(result, total)
        return
    for i in range(N):
        if visit[i] == 1:
            continue
        visit[i] = 1
        dis = abs(customer[i][0]-now[0])+abs(customer[i][1]-now[1])
        sell([customer[i][0], customer[i][1]], visit, total+dis, n+1)
        visit[i] = 0
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = list(map(int, input().split()))
    home = [M[0], M[1]]
    work = [M[2], M[3]]
    customer = [[M[2*i], M[2*i+1]] for i in range(2, len(M)//2)]
    result = 200*N
    for i in range(N):
        sell(work, [0]*N, 0, 0)
        customer.append(customer.pop())
    print('#{} {}'.format(tc, result))