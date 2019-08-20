import sys
sys.stdin = open("문자열비교.txt")
T = int(input())
for test_case in range(1, T+1):
    A = input()
    B = input()
    result = 0
    for i in range(len(B)-len(A)+1):
        if A[0] == B[i]:
            for j in range(1, len(A)):
                if A[j] != B[i+j]:
                    break
                if j == len(A)-1:
                    result = 1
    if result == 1:
        print('#{} 1'.format(test_case))
    else:
        print('#{} 0'.format(test_case))