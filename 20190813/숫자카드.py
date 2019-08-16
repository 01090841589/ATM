import sys
sys.stdin = open("numcard.txt")
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    n = input()
    max_num = 0
    num = 0
    for i in range(10):
        if n.count(str(i)) >= max_num:
            max_num = n.count(str(i))
            num = i
    print('#{0} {1} {2}'.format(test_case,num,n.count(str(num))))