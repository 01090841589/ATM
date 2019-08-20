
T = 10
for test_case in range(1, T+1):
    N, password = input().split()
    password = list(password)
    while True:
        a = len(password)
        for i in range(len(password)-1):
            if password[i] == password[i+1]:
                del password[i+1]
                del password[i]
                break
        if len(password) == a:
            break
    print('#{} {}'.format(test_case, ''.join(password)))