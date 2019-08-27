import sys
sys.stdin = open("ladder.txt")
DIR = [[0, -1], [0, 1], [-1, 0]]
def find_ladder(y, x):
    global result
    if y == 0:
        result = x
        return
    for arr in DIR:
        X, Y = x+arr[1], y+arr[0]
        if 0 <= X < 100 and 0 <= Y < 100:
            if ladder[Y][X] == 1:
                ladder[Y][X] = 2
                return find_ladder(Y, X)
for test_case in range(10):
    t = int(input())
    ladder = [list(map(int,input().split())) for i in range(100)]
    x = [i for i in range(100) if ladder[99][i] == 2]
    y, result = 99, 0
    find_ladder(y, x[0])
    print('#{0} {1}'.format(t,result))