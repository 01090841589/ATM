T = int(input())
for test_case in range(1, 1+T):
    word = input()
    poss = 0
    for k in range(len(word)):
        if k == len(word)-1:
            poss = 1
        if word[k] == word[len(word)-k-1]:
            continue
        elif word[k] == '*' or word[len(word)-k-1] == '*':
            poss = 1
            break
        else :
            break
    if poss :
        print('#{} Exist'.format(test_case))
    else :
        print('#{} Not exist'.format(test_case))