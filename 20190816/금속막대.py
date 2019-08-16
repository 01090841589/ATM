import sys
sys.stdin = open("금속막대.txt")
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    driver = list(map(int,input().split()))
    connect = []
    for i in range(0, N):
        for j in range(0, N):
            if driver[2*i] == driver[2*j+1]:
                break
            if j == N-1:
                connect += [driver[2*i],driver[2*i+1]]
    while True:
        for i in range(0, N):
            if connect[-1] == driver[2*i]:
                connect += [driver[2*i],driver[2*i+1]]
        if len(connect) == len(driver):
            break
    print('#{}'.format(test_case),end=' ')
    for i in connect:
        print(i,end=' ')
    print()
    