import sys
sys.stdin = open("부분집합의합.txt")
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
T = int(input())
for test_case in range(1, T+1):
    cnt =0
    N, K = map(int,input().split())
    for i in range(1, 1 << 12):
        sums = 0
        part = []
        nums = 0
        for j in range(12):
            if i & (1 << j):
                nums += 1
                sums += A[j]
                if nums > N:
                    break
        if sums == K and nums == N:
            cnt += 1

    print('#{0} {1}'.format(test_case,cnt))