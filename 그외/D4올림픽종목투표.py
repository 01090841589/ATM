import sys
sys.stdin = open("올림픽.txt")
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))
    select = [0]*N
    for num in Bi:
        for a in range(len(Ai)):
            if num >= Ai[a]:
                select[a] += 1
                break
    print('#{} {}'.format(test_case, select.index(max(select))+1))