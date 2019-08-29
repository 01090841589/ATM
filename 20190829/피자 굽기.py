import sys
sys.stdin = open('피자굽기.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int,input().split())
    Ci = list(map(int,input().split()))
    Ci_num, pizza = 1, [0]*N
    pizza_num = [i for i in range(1, T+1)]
    pizza = [[Ci.pop(0), pizza_num.pop(0)] for i in range(len(pizza))]
    print(pizza)
    while pizza:
        for i in range(N):
            pizza[i][0] //= 2
            if pizza[i][0] == 0 and len(Ci) > 0:
                pizza[i][0] = Ci.pop(0)
                pizza[i][1] = pizza_num.pop(0)
            if pizza.count(0) == (N-1):
                for a, b in enumerate(pizza):
                    if b > 0:
                        print('#{} {}'.format(test_case, pizza_num[a]))
                break