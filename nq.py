## import
import time

## global variable
N = 0
queen_info = []

result = 0

## function
def bruteForce(row, col,depth):
    global result
    global queen_info

    queen_info[0][row] = queen_info[1][col] = queen_info[2][row - col] = queen_info[3][row + col] = 1

    if depth == N-1 :
        result+=1

    else:
        for next_row in range(N):
            if not(queen_info[0][next_row] == 1 or queen_info[1][col+1] == 1 or queen_info[2][next_row - (col + 1)] == 1 or queen_info[3][next_row + col + 1] == 1):
                bruteForce(next_row, col+1,depth+1)

    queen_info[0][row] = queen_info[1][col] = queen_info[2][row - col] = queen_info[3][row + col] = 0

if __name__ == "__main__":
    N = int(input())

    for i in range(4):
        queen_info.append([0 for x in range(2*N - 1)])
    start_time = time.time()
    for i in range(N):
        bruteForce(i, 0,0)
    end_time = time.time()
    print("elapsed time : ", (end_time - start_time) * 1000 , "ms")
    print(result)