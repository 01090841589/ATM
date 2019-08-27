import sys
sys.stdin = open("contact.txt")
for tc in range(1, 11):
    length, N = list(map(int,input().split()))
    contect = list(map(int, input().split()))
    queue = [N]
    buf_queue = [N]
    contected = [N]
    visited = [0]*101
    visited[N] = 1
    final = []
    cnt = 1
    while buf_queue:
        queue = buf_queue[:]
        final = buf_queue[:]
        buf_queue = []
        while queue:
            N = queue.pop()
            for i in range(len(contect)//2):
                if contect[2*i] == N:
                    if visited[contect[2*i+1]] == 0:
                        buf_queue.insert(0, contect[2*i+1])
                        visited[contect[2*i+1]] = 1
                        contected.append(contect[2*i+1])
        cnt += 1
    print('#{} {}'.format(tc, max(final)))