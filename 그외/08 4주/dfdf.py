print(52/107)

print(520//107)
print(520%107)
print(920//107)
print(920%107)
for x in range(10):
    a, b = map(int, input().split())
    result = ''
    a %= b
    for i in range(100):
        c, d = divmod(a*10, b)
        if c == 0:
            break
        print(c, end='')
        result += str(c)
        a = d
    print()
    print(result)