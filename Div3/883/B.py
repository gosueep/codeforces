# from collections import defaultdict

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        board = [input() for i in range(3)]
        # print(board)
        
        lines = []
        for i in range(3):
            lines.append(board[i])
            vert = f'{board[0][i]}{board[1][i]}{board[2][i]}'
            lines.append(vert)
        diag1 = ''
        diag2 = ''
        for i in range(3):
            diag1 += board[i][i]
            diag2 += board[i][3-i-1]
        lines.append(diag1)
        lines.append(diag2)
        # print(lines)
        
        draw = True
        for line in lines:
            start = line[0]
            if start == '.':
                continue
            win = True
            for i in line:
                if i != start:
                    win = False
                    break
            if win:
                print(start)
                draw = False
                break
        if draw:
            print('DRAW')
        