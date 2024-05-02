n, q = map(int, input().split())

board = [[0] + list(map(int, input().split())) for _ in range(n)]
board.insert(0, [0 for _ in range(n+1)])

for row in board:
    for i in range(1, len(row)):
        row[i] += row[i-1]

for j in range(n+1):
    for i in range(1, n+1):
        board[i][j] += board[i-1][j]
        

for _ in range(q):
    y1, x1, y2, x2 = map(int, input().split())
    total = board[y2][x2] - (board[y2][x1-1] + board[y1-1][x2] - board[y1-1][x1-1])
    print(total)