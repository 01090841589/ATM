import sys
sys.stdin = open("계산기.txt")
for tc in range(1, 5):
    N = int(input())
    cal = list(input())
    icp = ['', '+', '*' ,'(']
    isp = ['(', '+', '*', '']
    interp = ['+', '*', '(', ')']
    stack = []
    word = []
    flag = 0
    for i in cal:
        print(stack, word)
        if i in interp:
            if stack == []:
                stack.append(i)
            elif i == ')':
                print(stack, word)
                while True:
                    k = stack.pop()
                    if k == '(':
                        break
                    else:
                        word.append(k)
            elif icp.index(i) > isp.index(stack[-1]):
                stack.append(i)
            else:
                while stack:
                        if icp.index(i) <= isp.index(stack[-1]):
                            word.append(stack.pop())
                            break
                word.append(i)

        else:
            word.append(int(i))
    while stack:
        word.append(stack.pop())
    print(stack, word)
    for A in word:
        if A == '+':
            stack.append((int(stack.pop())+int(stack.pop())))
        elif A == '*':
            stack.append((int(stack.pop())*int(stack.pop())))
        else:
            stack.append(A)
    print(stack[-1])