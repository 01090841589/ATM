T = int(input())
for test_case in range(1, T+1):
    a = input()
    b = input()
    alpa = dict()
    many = 0
    for ch in a:
        alpa[ch] = 0
    for ch in b:
        if ch in a:
            alpa[ch] += 1
    for num in alpa.values():
        if num > many:
            many = num
    print('#{} {}'.format(test_case,many))