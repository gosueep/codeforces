# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        line = input().strip()
        a,b,c = line
        if a=='a' or b=='b' or c=='c':
            print("YES")
        else:
            print('NO')
            