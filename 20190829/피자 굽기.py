import sys
sys.stdin = open('피자굽기.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int,input().split())
    Ci = list(map(int,input().split()))
    Ci_num = 1
    pizza = [0]*N
    pizza_num = [0]*N
    for i in range(len(pizza)):
        pizza[i] = Ci.pop(0)
        pizza_num[i] = Ci_num
        Ci_num += 1
    while pizza.count(0) != (N-1):
        for i in range(N):
            pizza[i] //= 2
            if pizza[i] == 0 and len(Ci) > 0:
                pizza[i] = Ci.pop(0)
                pizza_num[i] = Ci_num
                Ci_num += 1
            if pizza.count(0) == (N-1):
                for a, b in enumerate(pizza):
                    if b > 0:
                        print('#{} {}'.format(test_case, pizza_num[a]))
                break