def cal(a, b, eq):
    if eq == '+':
        return a + b
    elif eq == '*':
        return a * b
isp = {'+': 1, '*': 2, '(': 0}
nums = ['0', '1', '2', '3', '4' ,'5', '6', '7', '8', '9']
for tc in range(1, 11):
    N = int(input())
    arith = input()
    word = []
    stack = []
    for letter in arith:
        if letter in nums:
            word.append(int(letter))
        else:
            if letter == '(':
                stack.append('(')
            elif letter == ')':
                while True:
                    tmp = stack.pop()
                    if tmp == '(':
                        break
                    word.append(tmp)
            else:
                if stack:
                    if isp[stack[-1]] > isp[letter]:
                        tmp2 = stack[-1]
                        while isp[tmp2] > isp[letter]:
                            word.append(stack.pop())
                            if not stack:
                                break
                            tmp2 = stack[-1]
                        stack.append(letter)
                    else:
                        stack.append(letter)
                else:
                    stack.append(letter)
    for i in range(len(stack)):
        word.append(stack.pop())
    result = 0
    cal_stack = []
    for letter in word:
        if type(letter) == int:
            cal_stack.append(letter)
        else:
            result = cal(cal_stack.pop(), cal_stack.pop(), letter)
            cal_stack.append(result)
    print('#{} {}'.format(tc, result))