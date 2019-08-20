T = int(input())
for test_case in range(1, T+1):
    frog = input()
    frog = list(frog)
    inv = [list() for _ in range(len(frog)//5+2)]
    a = 0
    while True:
        cnt = 0
        for i in range(len(frog)):
            if frog[i] != '':
               cnt += 1
        for i, croak in enumerate(frog):
            if len(inv[a]) % 5 == 0:
                if croak == 'c':
                    frog[i] = ''
                    inv[a].append('c')
            if len(inv[a]) % 5 == 1:
                if croak == 'r':
                    frog[i] = ''
                    inv[a].append('r')
            if len(inv[a]) % 5 == 2:
                if croak == 'o':
                    frog[i] = ''
                    inv[a].append('o')
            if len(inv[a]) % 5 == 3:
                if croak == 'a':
                    frog[i] = ''
                    inv[a].append('a')
            if len(inv[a]) % 5 == 4:
                if croak == 'k':
                    frog[i] = ''
                    inv[a].append('k')
        if len(inv[a]) % 5 != 0:
            a = -1
            break
        cnt2 = 0
        for i in range(len(frog)):
            if frog[i] != '':
               cnt2 += 1
        a += 1
        if cnt2 == 0:
            break
        if cnt == cnt2:
            a = -1
            break
    print('#{} {}'.format(test_case, a))