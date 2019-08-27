import sys
sys.stdin = open("Forth.txt")

T = int(input())
for tc in range(1, T+1):
    forth = list(map(str, input().split()))
    stack = []
    for A in forth:
        if A == '+':
            if len(stack) < 2:
                print('#{} error'.format(tc))
                break
            stack.append((int(stack.pop()) + int(stack.pop())))
        elif A == '-':
            if len(stack) < 2:
                print('#{} error'.format(tc))
                break
            aa = int(stack.pop())
            bb = int(stack.pop())
            stack.append(bb - aa)
        elif A == '*':
            if len(stack) < 2:
                print('#{} error'.format(tc))
                break
            stack.append((int(stack.pop()) * int(stack.pop())))
        elif A == '/':
            if len(stack) < 2:
                print('#{} error'.format(tc))
                break
            aa = int(stack.pop())
            bb = int(stack.pop())
            stack.append(bb // aa)
        elif A == '.':
            if len(stack) == 1:
                print('#{} {}'.format(tc, stack.pop()))
            else:
                print('#{} error'.format(tc))
        else:
            stack.append(A)