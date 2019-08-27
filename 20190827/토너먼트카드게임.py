import sys
sys.stdin = open("토너먼트카드게임.txt")

def torna(battle, n):
    global result
    if len(battle) > 2:
        torna(battle[:(1+len(battle))//2], n)
        torna(battle[(1+len(battle))//2:], n+(1+len(battle))//2)
    else:
        if len(battle) == 1:
            battle = battle[0]
            result += battle
            result_num.append(n)
        else:
            if battle[0] == '1':
                if battle[1] == '1':
                    battle = '1'
                    result += battle
                    result_num.append(n)
                elif battle[1] == '2':
                    battle = '2'
                    result += battle
                    n += 1
                    result_num.append(n)
                else :
                    battle = '1'
                    result += battle
                    result_num.append(n)
            elif battle[0] == '2':
                if battle[1] == '1':
                    battle = '2'
                    result += battle
                    result_num.append(n)
                elif battle[1] == '2':
                    battle = '2'
                    result += battle
                    result_num.append(n)
                else :
                    battle = '3'
                    result += battle
                    n += 1
                    result_num.append(n)
            else :
                if battle[1] == '1':
                    battle = '1'
                    result += battle
                    n += 1
                    result_num.append(n)
                elif battle[1] == '2':
                    battle = '3'
                    result += battle
                    result_num.append(n)
                else :
                    battle = '3'
                    result += battle
                    result_num.append(n)

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    card_list = list(map(str, input().split()))
    card = ''.join(card_list)
    nums = [i for i in range(n)]

    while len(nums) > 1:
        result = ''
        result_num = []
        torna(card, 0)
        card = result
        card_result = []
        for i in result_num:
            card_result.append(nums[i])
        nums = card_result
    print('#{} {}'.format(test_case, int(nums[0])+1))