import sys
sys.stdin = open("bus.txt")
T = int(input())
for test_case in range(1, T+1):
    K, N, M = map(int, input().strip().split())
    stop = list(map(int, input().strip().split()))
    stop.append(N)
    locate = 0
    charge = 0
    for bus in range(M+1):
        for now in range(K,-1,-1):
            if locate+now in stop:
                locate += now
                charge += 1
                break
        if locate == N:
            print('#{} {}'.format(test_case, charge-1))
            break
    if locate != N:
        print('#{} 0'.format(test_case))