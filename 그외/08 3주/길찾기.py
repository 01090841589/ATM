import sys
sys.stdin = open("길찾기.txt")
for tc in range(1, 11):
    A = list(map(int,input().split()))
    route = list(map(int, input().split()))
    now = 0
    visited = [0]*101
    visited[0] = 1
    stack = []
    while True:
        for a in range(len(route)//2):
            if route[2*a] == now:
                if visited[route[2*a+1]] == 0:
                    stack.append(route[2*a+1])
                    visited[route[2*a+1]] = 1
        now = stack.pop()
        if now == 99:
            print('#{} 1'.format(tc))
            break
        if stack == []:
            print('#{} 0'.format(tc))
            break