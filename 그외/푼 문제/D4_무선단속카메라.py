import sys
sys.stdin = open("무선.txt")
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    K = int(input())
    locate = list(map(int,input().split()))
    locate = sorted(list(set(locate)))
    print(locate)
    dis = []
    if len(locate) > K:
        for i in range(len(locate)-1):
            dis.append(locate[i+1]-locate[i])
            print(dis)
        for a in range(K-1):
            dis.remove(max(dis))
            print(dis)
    print('#{0} {1}'.format(test_case,sum(dis)))