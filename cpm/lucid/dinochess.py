m,n  = map(int, input().split())

board = [[0 for x in range(n)] for y in range(n)]
dinos = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            possible = True
            for x,y in [(i+m,j), (i-m,j), 
                        (i,j+m), (i,j-m), 
                        (i+m, j+m), (i+m, j-m), 
                        (i-m, j+m), (i-m, j-m)]:
                if x < n and x >= 0 and y < n and y >= 0:
                    if board[x][y] != 0:
                        possible = False
                        break
            
            if possible:
                dinos += 1
                board[i][j] = 1
print(dinos)