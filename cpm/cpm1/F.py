# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N,x = map(int, input().split())
        wins = set(map(int, input().split()))
        
        i =0
        while x > 0:
            i+=1
            if i not in wins:
                x -= 1
        while i+1 in wins:
            i += 1
        print(i)
