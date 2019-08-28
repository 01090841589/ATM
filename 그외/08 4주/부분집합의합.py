import sys
sys.stdin = open("부분집합의합.txt")
T = int(input())
def size_sum(cnt, total, remain):
    global N, result, MAX, K
    if K == total:
        result += 1
        return
    if cnt == N:
        return
    if total+remain < K:
        return
    size_sum(cnt+1, total+A[cnt], remain-A[cnt])
    size_sum(cnt+1, total, remain-A[cnt])


for test_case in range(1, T+1):
    result = 0
    N, K = map(int,input().split())
    A = [i for i in range(1, N+1)]
    MAX = sum(A)
    size_sum(0, 0, MAX)
    print('#{0} {1}'.format(test_case,result))
