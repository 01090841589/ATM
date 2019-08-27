import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    genes = input().rstrip().split()

    health = list(map(int, input().rstrip().split()))

    s = int(input())

    MAX = 0
    MIN = 10000000
    for s_itr in range(s):
        firstLastd = input().split()

        first = int(firstLastd[0])

        last = int(firstLastd[1])

        d = firstLastd[2]
        total = 0
        for comp in range(first, last+1):
            if genes[comp] in d:
                for i in range(len(d)-len(genes[comp])+1):
                    if d[i:i+len(genes[comp])] == genes[comp]:
                        total += health[comp]
                print(genes[comp], total)
        if total < MIN:
            MIN = total
        if total > MAX:
            MAX = total
    print(MIN, MAX)