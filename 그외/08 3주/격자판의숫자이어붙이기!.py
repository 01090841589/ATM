import sys
sys.stdin = open("격자판.txt")
DIR = [[1, 0], [0, 1], [-1, 0], [0, -1]]
def seven(y, x, nums, n):
    global total
    if n >= 7:
        total.append(''.join(nums))
        return
    for c in range(4):
        Y = y+DIR[c][0]
        X = x+DIR[c][1]
        if 0 <= X < 4 and 0 <= Y < 4:
            nums[n] = mat[Y][X]
            seven(Y, X, nums, n+1)
T = int(input())
for tc in range(1, T+1):
    mat = [list(input().split()) for _ in range(4)]
    total = []
    for a in range(4):
        for b in range(4):
            seven(a, b, [mat[a][b], 0, 0, 0, 0, 0, 0], 1)
    total = list(set(total))
    print('#{} {}'.format(tc, len(total)))