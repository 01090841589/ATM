def versus(a, b, c, d):
    if a == 1:
        if b == 1:
            return a, c
        elif b == 2:
            return b, d
        else:
            return a, c
    elif a == 2:
        if b == 1:
            return a, c
        elif b == 2:
            return a, c
        else:
            return b, d
    else:
        if b == 1:
            return b, d
        elif b == 2:
            return a, c
        else:
            return a, c
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    toner = list(map(int, input().split()))
    nums = []
    for i in range(1, len(toner)+1):
        nums.append(i)
    while len(nums)>1:
        final = []
        final_nums = []
        for i in range(len(toner)//2):
            result = versus(toner[i*2],toner[i*2+1], nums[i*2], nums[i*2+1])
            final.append(result[0])
            final_nums.append(result[1])
        if len(toner)%2:
            final.append(toner[-1])
            final_nums.append(nums[-1])
        toner = final
        nums = final_nums
    print('#{} {}'.format(test_case, nums[0]))