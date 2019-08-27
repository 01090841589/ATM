T = 10
for tc in range(1, T+1):
    n = int(input())
    word = [input() for _ in range(8)]
    cnt = 0
    for i in range(8):
        for j in range(8 - n + 1):
            for k in range(n // 2):
                if word[i][j + k] != word[i][j + n - k - 1]:
                    break
                if k == n // 2 - 1:
                    cnt += 1
    for i in range(8):
        for j in range(8 - n + 1):
            for k in range(n // 2):
                if word[j + k][i] != word[j + n - k - 1][i]:
                    break
                if k == n // 2 - 1:
                    cnt += 1
    print('#{} {}'.format(tc,cnt))