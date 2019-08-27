bin_num = ['00', '01', '10', '11']
T = int(input())
for test_case in range(1, T+1):
    a, b, c, d = map(int,input().split())
    total = a+b+c+d
    password = ''
    anum = '0' + '0'*a
    dnum = '1' + '1'*d
    a = 0
    d = 0
    for i in range(b+c):
        if c >= b:
            if password == '':
                password += bin_num[2]
                c -= 1
            elif password[0] == '0':
                password = bin_num[2][0] + password
                c -= 1
            if len(dnum)>0:
                password = dnum + password[1:]
                dnum = ''
        elif b > c:
            if password == '':
                password += bin_num[1]
                b -= 1
            elif password[0] == '1':
                password = bin_num[1][0] + password
                b -= 1
            if len(anum)>0:
                password = anum + password[1:]
                anum = ''
    if dnum != '' and password != '':
        if password[0] == '1':
            password = dnum + password[1:]
        elif password[-1] == '1':
            password = password + dnum[1:]
    if anum != ''and password != '':
        if password[0] == '0':
            password = dnum + password[1:]
        elif password[-1] == '0':
            password = password + anum[1:]

    if len(password)-1 == total:
        print('#{} {}'.format(test_case,password))
    else:
        print('#{} impossible'.format(test_case))

