import sys
sys.stdin = open("병합정렬.txt")

def torna(battle, n):
    global result
    if len(battle) > 2:
        print(battle[:(len(battle))//2],battle[(len(battle))//2:])
        print(battle[(len(battle))//2-1], battle[-1])
        if battle[(len(battle))//2-1] > battle[-1]:
            result += 1
        torna(battle[:(len(battle))//2], n)
        torna(battle[(len(battle))//2:], n+(len(battle))//2)
    elif len(battle) == 2:
        print(battle[0], battle[1])
        if battle[0] > battle[1]:
            result += 1
    else :
        return

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    card = list(map(int, input().split()))
    nums = [i for i in range(n)]

    while len(nums) > 1:
        result = 0
        result_num = []
        torna(card, 0)
        card = result
        card_result = []
        for i in result_num:
            card_result.append(nums[i])
        nums = card_result
    print('#{} {}'.format(test_case, result))