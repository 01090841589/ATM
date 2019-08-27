import sys
sys.stdin = open("줄세우기.txt")
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    i = 0
    while i < N:
        print(i,end=' ')
        print(arr[i])
        if N-arr[i] <= result:
            i += 1
            continue
        print(i)
        cnt = 1
        buf = arr[i]
        j = 0
        while j < N:
            if arr[j] == buf+1:
                buf += 1
                cnt += 1
            j += 1
        if cnt > result:
            result = cnt
        i += 1
    print(cnt)
    print('#{} {}'.format(test_case, N-result))