T = int(input())
for test_case in range(1, T+ 1):
    A, B, C, D = map(int, input().split())
    if abs(B - C) > 1 or (B + C == 0 and A != 0 and D != 0):
        print('#{} impossible'.format(test_case))
        continue
    result = ''
    if B == 0 and C == 0:
        if A:
            result = '0' * (A + 1)
        elif D:
            result = '1' * (D + 1)
    elif B == C:
        result = '0' * A + '01' * B + '1' * D + '0'
    elif B > C:
        result = '0' * A + '01' * B + '1' * D
    else:
        result = '1' * D + '10' * C + '0' * A

    print('#{} {}'.format(test_case, result))