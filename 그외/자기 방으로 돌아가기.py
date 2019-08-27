import sys
sys.stdin = open("자기방.txt")
T = int(input())
for test_case in range(1, T+1):
    corridir = [0] * 201
    result = 0
    N = int(input())
    student = [sorted(list(map(int, input().split()))) for _ in range(N)]
    for i in range(N):
        for j in range((student[i][0]+1)//2, (student[i][1]+1)//2+1):
            corridir[j] += 1
    for i in range(len(corridir)):
        if corridir[i] > result:
            result = corridir[i]
    print('#{} {}'.format(test_case,result))