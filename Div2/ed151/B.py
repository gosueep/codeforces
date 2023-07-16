# from collections import defaultdict


def shared(dx, dy):
    if (dx > 0 and dy > 0) or (dx<0 and dy<0):
        return min(abs(dx), abs(dy))
    return 0
         

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        ax, ay = map(int, input().split())
        bx, by = map(int, input().split())
        cx, cy = map(int, input().split())
        
        together = 1 + shared(bx-ax, cx-ax) + shared(by-ay, cy-ay)
        
        print(together)