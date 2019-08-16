import sys
sys.stdin = open("flatten.txt")
for test_case in range(1,11):
    N = int(input())
    num = list(map(int,input().split()))
    for i in range(N):
        max_num = 0
        min_num = 100
        max_ind = 0
        min_ind = 0
        for comp_index in range(100):
            if num[comp_index] > max_num:
                max_num = num[comp_index]
                max_ind = comp_index
            if num[comp_index] < min_num:
                min_num = num[comp_index]
                min_ind = comp_index
        num[max_ind] -= 1
        num[min_ind] += 1
    max_num = 0
    min_num = 100
    for comp_index in range(100):
        if num[comp_index] > max_num:
            max_num = num[comp_index]
        if num[comp_index] < min_num:
            min_num = num[comp_index]
    print('#{} {}'.format(test_case, max_num - min_num))