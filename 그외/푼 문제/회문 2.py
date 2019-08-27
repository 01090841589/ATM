for tc in range(1, 11):
    N = int(input())

    arr = [input() for _ in range(100)]

    ans = 0

    for rc in range(100):
        for s in range(100):
            l, r, cnt = s, s + 1, 0
            while l >= 0 and r < 100:
                if arr[rc][l] != arr[rc][r]: break
                cnt += 2
                l, r = l - 1, r + 1
            ans = max(ans, cnt)

            l, r, cnt = s, s + 1, 0
            while l >= 0 and r < 100:
                if arr[l][rc] != arr[r][rc]: break
                cnt += 2
                l, r = l - 1, r + 1
            ans = max(ans, cnt)

            l, r, cnt = s - 1, s + 1, 1
            while l >= 0 and r < 100:
                if arr[rc][l] != arr[rc][r]: break
                cnt += 2
                l, r = l - 1, r + 1
            ans = max(ans, cnt)

            l, r, cnt = s - 1, s + 1, 1
            while l >= 0 and r < 100:
                if arr[l][rc] != arr[r][rc]: break
                cnt += 2
                l, r = l - 1, r + 1
            ans = max(ans, cnt)

    print('#{} {}'.format(tc, ans))