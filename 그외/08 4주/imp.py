import sys
sys.stdin = open("shuffle.txt")

for tc in range(1, 11):
    V, E = map(int, input().split())
    line = list(map(int, input().split()))
    cnt = 1
    link = []
    while line:
        i = 0
        stack = []
        visit = [0] * (V+1)
        for i in range(len(line)//2):
            visit[line[2*i+1]] += 1
        for j in range(1, len(visit)):
            if visit[j] == 0:
                stack.append(j)
                if j not in link:
                    link.append(j)
            stack.sort(reverse=True)
            for i in range(len(line)//2-1, -1, -1):
                if line[2*i] in stack:
                    line.pop(2*i)
                    line.pop(2*i)
    for i in range(1, V+1):
        if i not in link:
            link.append(i)

    print('#{} {}'.format(tc, ,' '.join(list(map(str, link)))))
