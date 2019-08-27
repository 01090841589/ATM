for test_case in range(1, 11):
    t = int(input())
    wo = input()
    word = input()
    i = 0
    j = 0
    cnt = 0
    while j < len(wo) and i < len(word):
        if word[i] != wo[j]:
            i = i - j
            j = -1
        i = i+1
        j = j+1
        if j == len(wo) :
            cnt += 1
            j = 0
    print('#{} {}'.format(test_case,cnt))