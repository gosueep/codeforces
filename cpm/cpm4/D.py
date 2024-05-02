# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        
        out = []
        for i in range(N//2+1):
            out.append(i)
            out.append(i+2)
        
        print(out[:N])
    
        