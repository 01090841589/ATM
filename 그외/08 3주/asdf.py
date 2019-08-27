import itertools
N = 3
for p in itertools.permutations(range(N)):
    for i in range(N):
        print(p[i], end=" ")
    print()