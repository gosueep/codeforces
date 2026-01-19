from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        B = list(map(int, input().split()))

        counts = defaultdict(int)
        for x in B:
            counts[x] += 1
        
        works = True
        for key, value in counts.items():
            if key != value:
                works = False
        
        print(counts)

        if works:
            print(' '.join([str(x) for x in B]))
        else:
            print(-1)