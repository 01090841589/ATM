T = int(input())
for test_case in range(1, T+1):
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    total = nums[0]
    result = []
    for a in range(0, 7):
        for b in range(a+1, 7):
            for c in range(b+1, 7):
                result.append(nums[c]+nums[a]+nums[b])
    result = list(set(result))
    result.sort(reverse=True)
    print('#{} {}'.format(test_case, result[4]))