# from collections import defaultdict

def candy():
    instrs = int(input())
    x, y = 0, 0
    dirs = {
        'U': (0, 1),
        'D': (0, -1),
        'R': (1, 0),
        'L': (-1, 0)
    }
    for i in input():
        x += dirs[i][0]
        y += dirs[i][1]
        if (x, y) == (1, 1):
            return 'YES'
    return 'NO'


if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        print(candy())



