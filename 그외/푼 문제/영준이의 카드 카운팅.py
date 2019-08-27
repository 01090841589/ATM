T = int(input())
for test_case in range(1, T+1):
    S = [0]+[1]*13
    D = [0]+[1]*13
    H = [0]+[1]*13
    C = [0]+[1]*13
    error = 0
    card = input()
    for i in range(0, len(card), 3):
        if card[i] == 'S':
            if S[int(card[i+1]+card[i+2])] != 0:
                S[int(card[i+1]+card[i+2])] = 0
            else:
                error = 1
        if card[i] == 'D':
            if D[int(card[i+1]+card[i+2])] != 0:
                D[int(card[i+1]+card[i+2])] = 0
            else:
                error = 1
        if card[i] == 'H':
            if H[int(card[i+1]+card[i+2])] != 0:
                H[int(card[i+1]+card[i+2])] = 0
            else:
                error = 1
        if card[i] == 'C':
            if C[int(card[i+1]+card[i+2])] != 0:
                C[int(card[i+1]+card[i+2])] = 0
            else:
                error = 1
    if error :
        print('#{} ERROR'.format(test_case))
    else:
        print('#{} {} {} {} {}'.format(test_case, sum(S), sum(D), sum(H), sum(C)))