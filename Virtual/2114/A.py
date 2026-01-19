# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        t = int(input())
        root = int(t**.5)
        if root*root == t: 
            print(int(root), 0)
        else:
            print(-1)