# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        b, c, h = map(int, input().split())
        
        layers = 3
        b -= 2
        f = c + h -1
        layers += 2*min(b, f)
        
        print(layers)