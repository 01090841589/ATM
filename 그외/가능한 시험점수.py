import sys
sys.stdin = open("시험.txt")

T = int(input())
for test_case in range(1, T+1):
    N = input()
    score = list(map(int, input().split()))
    sums = {0}
    for i in score:
        for j in list(sums):
            sums.add(j + i)
    print("#{} {}".format(test_case, len(sums)))