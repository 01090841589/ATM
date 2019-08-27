import sys
sys.stdin = open("일분배.txt")
def work_div(N, cnt, gone, total):
    global result
    if total < result and result <1:
        return
    if cnt >= N:
        if result == 1:
            result = total
        else:
            result = max(result, total)
            return
    for i in range(N):
        if gone[i] == 1:
            continue
        gone[i] = 1
        work_div(N, cnt + 1, gone, total*(mat[cnt][i]/100))
        gone[i] = 0
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(n)]
    result = 1
    work_div(n, 0, [0]*n, 1)

    print("#%s %0.6f" %(test_case, result*100))