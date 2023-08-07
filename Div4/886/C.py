# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        
        N=8
        output = ''
        for i in range(N):
            for c in input().strip():
                if c != '.':
                    output += c
        print(output)
                