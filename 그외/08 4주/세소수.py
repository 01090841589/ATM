n = 997
a = [0, 0] + [1] * (n - 1)
primes = []
for i in range(2, n + 1):
    if a[i]:
        primes.append(i)
        for j in range(2 * i, n + 1, i):
            a[j] = False
length = len(primes)
T = int(input())
for tc in range(1, T+1):
    result = []
    n = int(input())
    cnt = 0
    for i in range(length):
        if primes[i] >= n:
            break
        for j in range(i, length):
            if primes[i]+primes[j] >= n:
                break
            for k in range(j, length):
                if primes[i]+primes[j]+primes[k] == n:
                    cnt += 1
    print('#{} {}'.format(tc, cnt))