T = 10
for test_case in range(1, T+1):
    n = int(input())
    password = list(map(int, input().split()))
    while True:
        for j in range(1, 6):
            buf = password.pop(0) - j
            if buf <= 0:
                password.append(0)
                break
            else:
                password.append(buf)
        if buf <= 0:
            break
    print('#{} {}'.format(test_case, ' '.join(list(map(str,password)))))