def lis(arr):
    n = len(arr)
    lis = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    maximum = 0
    for i in range(n):
        maximum = max(maximum, lis[i])
    return maximum
# T = int(input())
# for test_case in range(1, T+1):
#     n = int(input())
#     print('#{} {}'.format(test_case,lis(list(map(int, input().split())))))
lis([1, 25, 213, 21, 523, 432, 568, 253, 432, 123, 5, 4, 43,2, 25, 23, 568, 25, 346])