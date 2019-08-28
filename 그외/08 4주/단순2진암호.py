import sys
sys.stdin = open("단순2진암호.txt")
password_map = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    mat = [str(input()) for _ in range(N)]
    # [print(mat[i]) for i in range(N)]
    # print()
    password = []
    for y in range(N-1, -1, -1):
        for x in range(M-1, -1, -1):
            if mat[y][x] == '1':
                for i in range(7*8):
                    password.insert(0, mat[y][x-i])
                break
        if password != []:
            break

    # print(''.join(password))
    decord = ''
    cord = ''
    for num in password:
        decord += num
        if len(decord) == 7:
            # print(decord)
            cord += str(password_map.index(decord))
            decord = ''
    total = (int(cord[0])+int(cord[2])+int(cord[4])+int(cord[6]))*3+int(cord[1])+int(cord[3])+int(cord[5])+int(cord[7])
    result = 0
    if total % 10 == 0:
        for a in cord:
            result += int(a)
        print('#{} {}'.format(tc, result))
    else:
        print('#{} {}'.format(tc, result))