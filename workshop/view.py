import sys
sys.stdin = open("view_input.txt")
def views(a):
    global view
    global i
    if a == 0:
        return 0
    if bu[i] - bu[i + a] < view:
        if bu[i] - bu[i + a] > 0:
            view = bu[i] - bu[i + a]
        else:
            view = 0
for tc in range(1,11):
    count = int(input())
    bu = list(map(int, input().split()))
    tot = 0
    for i in range(2, len(bu)-2):
        view = bu[i]
        for a in range(-2, 3):
            views(a)
        tot += view
    print('#{0} {1}'.format(tc,tot))