# def my_strrev(art):
#     ary = list(art)
#     for i in range(len(ary)//2):
#         ary[i], ary[-i-1] = ary[-i-1], ary[i]
#     return ''.join(ary)
#
#
# print(my_strrev('asdf'))

# def atoi(string):
#     value=0
#     i = 0
#     while (i < len(string)):
#         c = string[i]
#         if c >= '0' and c <= '9':
#             digit = ord(c) - ord('0')
#         else:
#             break
#         value = (value * 10 )+ digit
#         i += 1
#     return value
#
# print(atoi('123'))

# def itoa(x):
#     x = list(x)
#     num = 0
#     ten = 1
#     for i in range(len(x)-1, -1, -1):
#         num += (ord(x[i])-48) * ten
#         ten *= 10
#     return num
#
# print(type(itoa('123')))
# print(itoa('123'))
#
# def itoa(x):
#     nums = []
#     while True:
#         if x % 10 == 0:
#             break
#         num = x % 10
#         nums.append(chr(num+48))
#         x //= 10
#
#     return ''.join(nums)
# print(itoa(123))
# print(type(itoa(123)))




# word = 'TTTTAACCA'
# pat = 'TTA'
# for i in range(len(word)-(len(pat)-1):


def Bbit_print(a):
    for i in range(7, -1, -1):
        if a & (1<<i):
            print(1, end='')
        else:
            print(0, end='')
    print()

a = 0x86
key = 0xAA
print("a      ==>", end=' ')
Bbit_print(a)

print("a^=key ==>", end=' ')
a ^= key
Bbit_print(a)

print("a^=key ==>", end=' ')
a ^= key
Bbit_print(a)

