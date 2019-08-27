# import sys
# sys.stdin = open("bread.txt")
T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int,input().split())
    ctm =list(map(int,input().split()))
    ctm.sort()
    error = 0
    bread = 0
    for i in range(1, max(ctm)+1):
        if i % M == 0:
            bread += K
        while True:
            if i in ctm:
                bread -= 1
                ctm.remove(i)
                if bread < 0:
                    error = 1
                    break
            else :
                break
        if bread < 0:
            error = 1
            break
    if 0 in ctm:
        error = 1
    if error :
        print("#{} Impossible".format(test_case))
    else :
        print("#{} Possible".format(test_case))
