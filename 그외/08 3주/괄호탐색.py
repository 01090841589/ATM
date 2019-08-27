import sys
sys.stdin = open("괄호.txt")
for test_case in range(1, 11):
    N = int(input())
    words = input()
    endoor = []
    for word in words:
        if word == ')':
            if endoor[-1] == '(':
                endoor.pop()
            else :
                break
        elif word == ']':
            if endoor[-1] == '[':
                endoor.pop()
            else :
                break
        elif word == '}':
            if endoor[-1] == '{':
                endoor.pop()
            else :
                break
        elif word == '>':
            if endoor[-1] == '<':
                endoor.pop()
            else :
                break
        else :
            endoor.append(word)
    if len(endoor) == 0:
        print('#{} 1'.format(test_case))
    else:
        print('#{} 0'.format(test_case))