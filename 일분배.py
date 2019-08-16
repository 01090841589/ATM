def search_num(N, cnt, gone, total):
    global result
    if total < result:
        return False
    if cnt >= N:
        result = max(result, total)
        return False
    for i in range(N):
        if gone[i] == 1:
            continue
        gone[i] = 1
        search_num(N, cnt+1 , gone, total*mat[cnt][i])
        gone[i] = 0
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    mat = []
    result = 0
    for j in range(n):
        per = list(map(int, input().split()))
        mat.append(list(map(lambda x : (100-x)/100, per)))
    search_num(n, 0, [0]*n, 1)

    print("#{} {}".format(test_case, result*100))