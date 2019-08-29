import sys
sys.stdin = open('색종이.txt')


def ractan_search(y, x):
    for i in range(5, 0, -1):
        if correct(y, x, i):
            for Y in range(i):
                for X in range(i):
                    papers.append([y+Y, x+X, i])


def correct(y, x, i):
    if x + i < 10 and y + i < 10:
        for Y in range(i):
            for X in range(i):
                if mat[y+Y][x+X] == 0:
                    return False
    else:
        return False
    return True


paper = [5, 5, 5, 5, 5]
T = int(input())
for tc in range(1, T+1):
    mat = [list(map(int, input().split())) for _ in range(10)]
    [print(mat[i]) for i in range(10)]

    papers = []
    for y in range(10):
        for x in range(10):
            if mat[y][x] == 1:
                ractan_search(y, x)
    print(papers)
    while papers:
        print(papers)
        flag = 0
        for i in range(len(papers)):
            for j in range(len(papers)):
                if [papers[i][0], papers[i][1]] == [papers[j][0], papers[j][1]] and i != j:
                    if papers[i][2] < papers[j][2] and correct(papers[j][0], papers[j][1], papers[j][2]):
                        papers.pop(i)
                        break
                    flag = 1
                    break
            if flag == 1:
                break
            else:
                print(papers[i][0], papers[i][1], papers[i][2], papers)
                if papers[i][2] > 1:
                    print(papers[i][0], papers[i][1], papers[i][2], papers)
                    if correct(papers[i][0], papers[i][1], papers[i][2]):
                        print(papers[i][0], papers[i][1], papers[i][2])
                        for y in range(papers[i][2]):
                            for x in range(papers[i][2]):
                                for k in range(len(papers)-1, -1, -1):
                                    if [papers[i][0]+y, papers[i][1]+x, papers[i][2]] == papers[k]:
                                        papers.pop(k)
                        papers.pop(i)
                        break
                    else:
                        print(papers[i][0], papers[i][1], papers[i][2])
                        papers.append(papers.pop(0))
                        break

                else:
                    paper[papers[i][2]] -= 1
                    papers.pop(i)
                    break
    print(paper)