import sys
sys.stdin = open("작업순사.txt")

for tc in range(1, 4):
    V, E = map(int, input().split())
    line = list(map(int, input().split()))
    cnt = 1
    stack = []
    visit = [0] * (V+1)
    for i in range(len(line)//2):
        visit[line[2*i+1]] += 1
    print(visit)
    for j in range(1, len(visit)):
        if visit[j] == 0:
            print(j,end=' ')
            for i in range(len(line)//2):
                if line[2*i] == j:
                    stack.append(i)
    print(stack, line)
    visit = [0] * (V+1)
    print()
    for i in range(len(line)//2):
        visit[line[2*i+1]] += 1
    print(visit)
    for j in range(1, len(visit)):
        if visit[j] == 0:
            print(j,end=' ')
    print()
