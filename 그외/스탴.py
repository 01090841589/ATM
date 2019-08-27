def pop():
    if len(s) == 0:
        return
    else :
        return s.pop(-1)
def push(item):
    s.append(item)

s = []

def check_(data):
    for i in data:
        if i == '(':
            push(i)
        else:
            if s == []:
                return -1
            elif pop() == '(':
                continue
            else:
                push(')')
        print(s)
check_('(())(())(()())()(())()(())(()')