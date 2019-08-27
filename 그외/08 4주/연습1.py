word = input()
cal = ['+', '-', '*', '/']
stack = []
for i in word:
    if i in cal:
        stack.append(i)
    else:
        print(i, end='')
for i in range(len(stack)):
    print(stack.pop(), end='')