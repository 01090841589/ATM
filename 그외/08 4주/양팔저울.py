import sys
sys.stdin = open("양팔저울.txt")

def comp_kg(k, left, right, kgs):
    global cnt
    if sum(left) < sum(right):
        return
    if k == N:
        # print(left, right)
        cnt += 1
        return
    else:
        comp_kg(k+1, left+[kgs[k]], right, kgs)
        comp_kg(k+1, left, right+[kgs[k]], kgs)



def powerset(k, n, l):      # n: 원소의 갯수, k: 현재depth

    if k == N:          # Basis Part
        # print(n)
        comp_kg(0, [], [], n)
    else:               # Inductive Part
        for i in range(len(kg)):
            if A[i] == 1:
                continue
            A[i] = 1        # k번 요소 O
            powerset(k+1, n + [kg[i]], l)  # 다음 요소 포함 여부 결정
            A[i] = 0       # k번 요소 X

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    kg = list(map(int, input().split()))
    A = [0 for _ in range(N)]  # 원소의 포함여부 저장 (0, 1)
    cnt = 0
    powerset(0, [], 0)
    print('#{} {}'.format(tc, cnt))
