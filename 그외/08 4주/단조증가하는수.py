T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    result_list = []
    tmp_list = []
    for j in range(N - 1):
        for k in range(j + 1, N):
            flag = 1
            tmp = num_list[j] * num_list[k]
            tmp_list = list(str(tmp))
            print(tmp_list)
            for k in range(len(tmp_list) - 1):
                if tmp_list[k] > tmp_list[k + 1]:
                    flag = 0
                    break
            if flag:
                print(result_list, tmp)
                result_list = result_list + [tmp]
    result = 0
    if len(result_list) == 0:
        result = -1
    else:
        for nums in result_list:
            if result < nums:
                result = nums
    print('#{} {}'.format(tc, result))