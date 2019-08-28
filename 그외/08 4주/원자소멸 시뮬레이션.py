import sys
sys.stdin = open("원자소멸.txt")
DIR = [[1, 0], [-1, 0], [0, -1], [0, 1]]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ball = [list(map( int,input().split())) for _ in range(N)]
    total = 0
    for a in range(len(ball)):
        ball[a][0], ball[a][1] = ball[a][1]*2, ball[a][0]*2
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
    print('#{} {}'.format(tc, total))