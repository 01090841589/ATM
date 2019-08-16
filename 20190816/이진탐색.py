import sys
sys.stdin = open("이진탐색.txt")
T = int(input())
for test_case in range(1, T+1):
    P,A,B = list(map(int,input().split()))
    lA = [1, P]
    lB = [1, P]

    while True:
        if int((lA[0]+lA[1])/2) < A:
            lA[0] = int((lA[0]+lA[1])/2)
        elif int((lA[0]+lA[1])/2) > A:
            lA[1] = int((lA[0]+lA[1])/2)
        else :
            lA[0],lA[1] = A, A
        if int((lB[0]+lB[1])/2) < B:
            lB[0] = int((lB[0]+lB[1])/2)
        elif int((lB[0]+lB[1])/2) > B:
            lB[1] = int((lB[0]+lB[1])/2)
        else :
            lB[0],lB[1] = B, B
        if lA[0] == A or lB[0] == B:
            break
    if lA[0] == A and lB[0] == B:
        print('#{0} 0'.format(test_case))
    elif lA[0] == A:
        print('#{0} A'.format(test_case))
    else:
        print('#{0} B'.format(test_case))