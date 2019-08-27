import time
start_time = time.time()
count = 0
N = 10
A = [0 for _ in range(N)]
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def printSet(n, sum):
    global count
    if sum == 10:
        count += 1
def powerset(n, k, sum):
    if n == k:
        printSet(n, sum)
    else:
        A[k] = 1
        powerset(n, k + 1, sum+data[k])
        A[k] = 0
        powerset(n, k + 1, sum)
powerset(N, 0, 0)
print(count)
print(time.time() - start_time, 'seconds')