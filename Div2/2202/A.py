from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        counts = defaultdict(int)
        for _ in range(N):
            for x in map(int, input().strip().split()):
                counts[x] += 1
        
        max_amt = (N**2)-N
        works = True
        for x, count in counts.items():
            if count > max_amt:
                works = False
        
        print(['NO','YES'][works])