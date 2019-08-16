import sys
sys.stdin = open("minmax.txt")
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    n = list(map(int, input().split()))
    min_num = 1000000
    max_num = 0
    for num in n:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num
    print('#{0} {1}'.format(test_case, max_num-min_num))