import math


if __name__ == '__main__':
    cases = int(input())

    for _ in range(cases):
        n, m = map(int, input().split())
        board = [[0 for x in range(n)] for y in range(n)]
        for _ in range(m):
            x, y = map(int, input().split())
            for i in range(n):
                board[i][y-1] += 1
                board[x-1][i] += 1

        # print(board)

        possible = False
        for row in board:
            for square in row:
                if square == 0:
                    possible = True

        print("YES") if possible else print("NO")


