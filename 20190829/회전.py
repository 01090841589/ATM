import sys
sys.stdin = open('회전.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int,input().split())
    words = list(map(int,input().split()))
    [words.append(words.pop(0)) for i in range(M)]
    print('#{} {}'.format(test_case, words[0]))