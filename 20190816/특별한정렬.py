import sys
sys.stdin = open("특별한정렬.txt")
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    nums = list(map(int,input().split()))
    for i in range(0, len(nums)-1):
        MIN = i
        MAX = i
        if i % 2:
            for j in range(i+1, len(nums)):
                if nums[MIN] > nums[j] :
                    MIN = j
            nums[i], nums[MIN] = nums[MIN], nums[i]
        else:
            for j in range(i+1, len(nums)):
                if nums[MAX] < nums[j] :
                    MAX = j
            nums[i], nums[MAX] = nums[MAX], nums[i]
    print('#{}'.format(test_case),end=' ')
    for i in range(10):
        print(nums[i],end=' ')
    print()