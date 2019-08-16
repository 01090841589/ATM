import sys
sys.stdin = open("ham.txt")
def taste(cal, n, choice, scr):
    global max_scr
    if cal > L:
        return
    for i in range(N):
        if max_scr < scr:
            print(cal, scr, choice)
            max_scr = scr
        if choice[i] == 1:
            break
        choice[i] = 1
        taste(cal+ham[i][1], n+1, choice, scr+ham[i][0])
        choice[i] = 0
T = int(input())
for test_case in range(1, T+1):
    N, L = map(int, input().split())
    ham = []
    [ham.append(list(map(int,input().split()))) for _ in range(N)]
    callorie = 0
    max_scr = 0
    taste(0, 0, [0]*N, 0)
    print('#{} {}'.format(test_case, max_scr))