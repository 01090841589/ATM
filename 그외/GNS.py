import sys
sys.stdin = open("GNS.txt")
nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())
for test_case in range(1, T+1):
    a, n = input().split()
    word = list(input().split())
    for i, wo in enumerate(word):
        for j, num in enumerate(nums):
            if wo == num:
                word[i] = j
    word.sort()
    for i, wo in enumerate(word):
        word[i] = nums[int(wo)]
    print('#{}'.format(test_case))
    print(' '.join(word))
