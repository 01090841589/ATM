import sys
sys.stdin = open("suffle.txt")

def shuffle(card, A, N):
    global answer, total
    if A > 5:
        return
    left = card[:N//2]
    right = card[N//2:]
    for i in range(N):
        if i < N//2:
            for k in range(i):
            result = []

            result = left[: (N//2)-i] + right[:i] + left[(N//2)-i:] + right[i:]
            # print(result, A)
            if result == answer:
                if total > A:
                    total = A
                return
            if result == answer2:
                if total > A:
                    total = A
                return
            if i != 0:
                shuffle(result, A+1, N)
        else:
            j = i - (N//2)
            result = right[: (N//2)-j] + left[:j] + right[(N//2)-j:] + left[j:]
            # print(result, A)
            if result == answer:
                if total > A:
                    total = A
                return
            if result == answer2:
                if total > A:
                    total = A
                return
            shuffle(result, A+1, N)
    # print()
    # for i in range(N):
    #     if i < N//2:
    #         result = left[: (N//2)-i] + right[:i] + left[(N//2)-i:] + right[i:]
    #     else:
    #         j = i - (N//2)
    #         result = right[: (N//2)-j] + left[:j] + right[(N//2)-j:] + left[j:]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(str, input().split()))
    answer = []
    answer2 = []
    for a in range(1, N+1):
        answer.append(str(a))
        answer2.insert(0, str(a))
    visited = []
    total = 6
    card = cards[:]
    if card == answer:
        total = 0
    if card == answer2:
        total = 0
    if total != 0:
        shuffle(card, 1, N)
    if total > 5:
        print('#{} -1'.format(tc))
    else:
        print('#{} {}'.format(tc, total))