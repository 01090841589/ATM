# T = int(input())
# for tc in range(T):
#     row, col = map(int, input().split())
#     data = [list(map(int, input().split())) for _ in range(row)]
#
# def isWall(x, y):
#     if 0 <= x < 5 and 0 <= y < 5:
#         return True
#     else:
#         return False
# def calAbs(y, x):
#     global sum
#     for i in range(4):
#         Y = y + DIR[i][0]
#         X = x + DIR[i][1]
#         if isWall(X, Y):
#             if arr[Y][X]-arr[y][x] > 0:
#                 sum += arr[Y][X]-arr[y][x]
#             else:
#                 sum -= arr[Y][X] - arr[y][x]
#
# arr = [list(map(int, input().split()))for _ in range(5)]
# DIR = [[0, 1], [0, -1], [1, 0], [-1, 0]]
# sum = 0
# for x in range(5):
#     for y in range(5):
#         calAbs(y, x)
# print(sum)

# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if i<j:
#             arr[i][j], arr[j][i] = arr[j][i] , arr[i][j]
# print(arr)

a = 'asasasdf'
print(a[1:3])
if 'as' in a:
    print(a)
print(a.count('as'))