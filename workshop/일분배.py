# import sys
# sys.stdin = open("work.txt")
def search_num(N, cnt, gone, total, work):
    global result
    global works
    if total > result:
        return False
    if cnt >= N:
        # if total < result:
        result = min(result, total)
        works = round(work*100,6)
        # else:
        #     works = round(work*100,6)
        return work
    for i in range(N):
        if gone[i] == 1:
            continue
        gone[i] = 1
        search_num(N, cnt + 1, gone, total+mat[cnt][i], work*(100-mat[cnt][i])/100)
        gone[i] = 0
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    mat = []
    works = 0
    result = 100*n
    for j in range(n):
        per = list(map(int, input().split()))
        mat.append(list(map(lambda x : (100-x), per)))
    search_num(n, 0, [0]*n, 0, 1)

    print("#{} {}".format(test_case, works))