import sys
sys.stdin = open("암호문2.txt")

for tc in range(1, 11):
    N = int(input())
    password = list(map(int, input().split()))
    M = int(input())
    command = list(map(str, input().split()))
    while command:
        com = command.pop(0)
        if com == 'I':
            K = int(command.pop(0))
            num = int(command.pop(0))
            for i in range(num):
                password.insert(K+i, int(command.pop(0)))
        if com == 'D':
            K = int(command.pop(0))
            num = int(command.pop(0))
            for i in range(num):
                password.pop(K)
    print('#{}'.format(tc),end=' ')
    [print(password[i], end=' ') for i in range(10)]
    print()