T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    dummy = []
    for A in range(n):
        dummy.append(int(input()))
    cnt = 0
    print(dummy)
    for a in range(10):
        if max(dummy) == min(dummy):
            break
        move = (max(dummy) - min(dummy)) // 2
        dummy[dummy.index(max(dummy))] -= move
        dummy[dummy.index(min(dummy))] += move
        cnt += move
        print(dummy)
    print('#{} {}'.format(test_case,cnt))