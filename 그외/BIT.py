import sys
sys.stdin = open("BIT.txt")
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    print('#{}'.format(tc),end=' ')
    for i in range(M):
        comm = list(map(int, input().split()))
        if comm[0] == 1:
            num[comm[1]-1] += comm[2]
        elif comm[0] == 2:
            print(sum(num[comm[1]-1:comm[2]+1]),end=' ')
    print()
    # print('#{} {}'.format(tc, tran+len(a)))