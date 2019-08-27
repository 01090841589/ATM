import sys
sys.stdin = open('ladder.txt')
def ladder(datas, N):
    start = []
    for i in range(N):
        if datas[0][i] == 1:
            start.append(i)

    for xsis in range(len(start)):  #시작점 하나씩 출발하면서 비교, X좌표가 움직이기 때문에 바뀌지 않는 처음X위치 지정
        count = 1
        # if start[xsis] == 0: #for문을 이용하여 모두 둘기 때문에 불필요한 중복요소 제거(있어도 작동)
        #     idx = xsis
        #     for j in range(count, N):
        #         if start[idx] != 99 and datas[j][start[idx]+1] == 1: #각
        #             idx += 1
        #         elif start[idx] != 0 and datas[j][start[idx] - 1] == 1:
        #             idx -= 1
        #         if datas[j][start[idx]] == 2:
        #             return start[xsis] #처음X위치 반환
        #         if j == 99:
        #             break
        # if start[xsis] == 99:
        #     idx = xsis
        #     for j in range(count, N):
        #         if start[idx] != 99 and datas[j][start[idx]+1] == 1:
        #             idx += 1
        #         elif start[idx] != 0 and datas[j][start[idx] - 1] == 1:
        #             idx -= 1
        #         if datas[j][start[idx]] == 2:
        #             return start[xsis]
        # elif start[xsis] != 0 and start[xsis] != 99:
        idx = xsis
        for j in range(count, N):
            if start[idx] != 99 and datas[j][start[idx]+1] == 1:
                idx += 1
            elif start[idx] != 0 and datas[j][start[idx]-1] == 1:
                idx -= 1
            if datas[j][start[idx]] == 2:
                return start[xsis]

T = 10
for _ in range(10):
    tc = int(input())

    datas = []
    for i in range(100):
        data = list(map(int, input().split()))
        datas.append(data)

    result = ladder(datas, 100)

    print('#{} {}'.format(tc, result))