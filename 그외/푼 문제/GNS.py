import sys
sys.stdin = open("GNS.txt")
nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for test_case in range(1, T+1):
    a, n = input().split()
    word = list(input().split())
    print('#{}'.format(test_case))
    [print(i,end=' ') for j in nums for i in word if i == j]
    print()