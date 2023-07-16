# from collections import defaultdict


dirs = {
    'UR': (1, 1),
    'UL': (-1, 1),
    'DR': (1, -1),
    'DL': (-1, -1)
}


if __name__ == '__main__':
    cases = int(input())

    for _ in range(cases):
        inp = input().split()
        # print(inp)
        n, m, i1, j1, i2, j2 = map(int, inp[:-1])
        dx, dy = dirs[inp[-1]]
        
        bounces = 0
        i, j = i1, j1
        while i != i2 and j != j2:
            i += dx
            j += dy
            
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                dx *= -1
                dy *= -1
                bounces += 1
            
            if bounces != 0 and i == i1 and j == j1 and (dx,dy) == dirs[inp[-1]]:
                bounces = -1
                break
            
        print(bounces)
