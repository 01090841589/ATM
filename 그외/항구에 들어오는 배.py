T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    day = []
    for i in range(N):
        day.append(int(input()))
    total = 0
    while True:
        buf = day[1] - day[0]
        times = 1
        arrive = 0
        while True:
            if 1+buf*times in day:
                day.remove(1+buf*times)
                arrive += 1
            if 1+buf*times > day[-1]:
                if arrive > 0:
                    total += 1
                break
            times += 1
        if len(day) == 1:
            break
    print('#{} {}'.format(test_case, total))