import sys
sys.stdin = open("matsum.txt")
DIR = [[0, 1], [1, 0], [1, 1], [1, -1]]

def max_sum(y, x, c):
    global max_num
    nsum = 0
    for _ in range(100):
        nsum += mat[y][x]
        y += DIR[c][0]
        x += DIR[c][1]
    if max_num < nsum:
        max_num = nsum
for test_case in range(1, 11):
    T = input()
    max_num = 0
    mat = [list(map(int,input().split())) for _ in range(100)]

    for i in range(100):
        max_sum(i, 0, 0)
    for j in range(100):
        max_sum(0, j, 1)
    max_sum(0,0,2)
    max_sum(0,99,3)
    print('#{} {}'.format(test_case,max_num))

a, b = map(int, input().split())
if a ==1:
    if b == 3:
        print('A')
    if b == 2:
        print('B')
elif a ==2:
    if b == 1:
        print('A')
    if b == 3:
        print('B')
else:
    if b == 1:
        print('A')
    if b == 2:
        print('B')