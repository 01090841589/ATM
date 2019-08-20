import sys
sys.stdin = open("회문2.txt")

def x_pelindrome(c):
    global result
    for i in range(100):
        for j in range(100):
            length = 0+c
            a = 0
            while j+1+a+c<100 and j-a>=0:
                if word[i][j-a] == word[i][j+1+a+c]:
                    length += 2
                    a += 1
                else:
                    break
            if length > result:
                result = length
def y_pelindrome(c):
    global result
    for i in range(100):
        for j in range(100):
            length = 0+c
            a = 0
            while j+1+a+c<100 and j-a>=0:
                if word[j-a][i] == word[j+1+a+c][i]:
                    length += 2
                    a += 1
                else:
                    break
            if length > result:
                result = length
T = 10
for tc in range(1, T+1):
    n = int(input())
    word = [input() for _ in range(100)]
    result = 0
    x_pelindrome(0)
    x_pelindrome(1)
    y_pelindrome(0)
    y_pelindrome(1)
    print('#{} {}'.format(tc,result))