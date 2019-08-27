T = int(input())
for tc in range(1, T+1):
    a = input()
    total = 1
    cnt = 1
    for i in range(len(a)-1):
        dis = 0
        if a[i] == a[i+1]:
            cnt = 2
            while True:
                dis += 1
                if 0 <= i-dis and i+1+dis < len(a):
                    if a[i-dis] == a[i+1+dis]:
                        cnt += 2
                    else:
                        break
                else:
                    break
            if cnt > total:
                total = cnt
    for i in range(len(a)-2):
        dis = 0
        if a[i] == a[i+2]:
            cnt = 3
            while True:
                dis += 1
                if 0 <= i-dis and i+2+dis < len(a):
                    if a[i-dis] == a[i+2+dis]:
                        cnt += 2
                    else:
                        break
                else:
                    break
            if cnt > total:
                total = cnt
    print('#{} {}'.format(tc, total))