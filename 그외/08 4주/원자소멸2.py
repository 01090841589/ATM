import sys
sys.stdin = open("원자소멸.txt")
DIR = [[1, 0], [-1, 0], [0, -1], [0, 1]]
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    ball = [list(map( int,input().split())) for _ in range(N)]
    total = 0
    for a in range(len(ball)):
        ball[a][0], ball[a][1] = ball[a][1]*2, ball[a][0]*2
    for a in range(len(ball)-1, -1, -1):
        flag = 0
        if ball[a][2] == 0:
            for b in range(len(ball)):
                if ball[b][2] == 1 :
                    if ball[b][1] == ball[a][1] and ball[a][0] < ball[b][0]:
                        flag = 1
                        break
                elif ball[b][2] == 2:
                    if ball[b][1]-ball[a][1] == ball[b][0]-ball[a][0] and ball[a][0] < ball[b][0]:
                        flag = 1
                        break
                elif ball[b][2] == 3:
                    if ball[a][1]-ball[b][1] == ball[b][0]-ball[a][0] and ball[a][0] < ball[b][0]:
                        flag = 1
                        break
        elif ball[a][2] == 1:
            for b in range(len(ball)):
                if ball[b][2] == 0:
                    if ball[b][1] == ball[a][1] and ball[a][0] > ball[b][0]:
                        flag = 1
                        break
                elif ball[b][2] == 2:
                    if ball[a][1]-ball[b][1] == ball[b][0]-ball[a][0] and ball[a][0] > ball[b][0]:
                        flag = 1
                        break
                elif ball[b][2] == 3:
                    if ball[b][1]-ball[a][1] == ball[b][0]-ball[a][0] and ball[a][0] > ball[b][0]:
                        flag = 1
                        break
        elif ball[a][2] == 2:
            for b in range(len(ball)):
                if ball[b][2] == 3:
                    if ball[b][0] == ball[a][0] and ball[a][1] > ball[b][1]:
                        flag = 1
                        break
                elif ball[b][2] == 0:
                    if ball[b][1]-ball[a][1] == ball[b][0]-ball[a][0] and ball[a][1] > ball[b][1]:
                        flag = 1
                        break
                elif ball[b][2] == 1:
                    if ball[a][1]-ball[b][1] == ball[b][0]-ball[a][0] and ball[a][1] > ball[b][1]:
                        flag = 1
                        break
        elif ball[a][2] == 3:
            for b in range(len(ball)):
                if ball[b][2] == 2:
                    if ball[b][0] == ball[a][0] and ball[a][1] < ball[b][1]:
                        flag = 1
                        break
                elif ball[b][2] == 0:
                    if ball[a][1]-ball[b][1] == ball[b][0]-ball[a][0] and ball[a][1] < ball[b][1]:
                        flag = 1
                        break
                elif ball[b][2] == 1:
                    if ball[b][1]-ball[a][1] == ball[b][0]-ball[a][0] and ball[a][1] < ball[b][1]:
                        flag = 1
                        break
        if flag == 0:
            del ball[a]
    for a in range(len(ball)):
        if ball[a][2] == 0:
            for b in range(len(ball)):
                if ball[b][2] == 0 and ball[a][0] <= ball[b][0]:
                    break
            lower = 2000
            for b in range(len(ball)):
                if ball[b][2] == 1 and ball[b][1] == ball[a][1] and ball[a][0] < ball[b][0] and lower:
                    break
    while len(ball) > 1:
        compare = []
        rem = []
        for a in range(len(ball)):
            ball[a][0], ball[a][1] = ball[a][0]+DIR[ball[a][2]][0], ball[a][1]+DIR[ball[a][2]][1]
            if [ball[a][0], ball[a][1]] not in compare:
                compare.append([ball[a][0], ball[a][1]])
            else:
                rem.append([ball[a][0], ball[a][1]])
        for a in range(len(ball)-1, -1, -1):
            if [ball[a][0], ball[a][1]] in rem:
                total += ball[a][3]
                del ball[a]
                continue
            if ball[a][0] < -2001 or ball[a][0] > 2001 or ball[a][1] < -2001 or ball[a][1] > 2001:
                del ball[a]
                continue
    # print(ball)
    print('#{} {}'.format(tc, total))