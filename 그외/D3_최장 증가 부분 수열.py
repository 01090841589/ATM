T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    long_part = []
    for i in range(1, 1<<n):
        sums = 0
        part = []
        for j in range(n):
            if i&(1<<j):
                if len(part) > 0:
                    if part[-1] < arr[j]:
                        part.append(arr[j])
                    else:
                        break
                else:
                    part.append(arr[j])
        if long_part == []:
            long_part = part
        elif len(long_part) < len(part) :
            long_part = part
    print('#{} {}'.format(test_case, len(long_part)))
