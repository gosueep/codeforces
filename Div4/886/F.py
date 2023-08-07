from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        lens = list(map(int, input().split()))
        
        count = defaultdict(int)
        for i in lens:
            count[i] += 1

        best = 0
        while lens:
            lens.sort(reverse=True)
            newlens = []
            hop = lens[0]
            caught = 0
            for i in lens[1:]:
                if hop % i == 0:
                    caught += 1
                else:
                    newlens.append(hop)
            best = max(caught, best)
            lens = newlens
        
        print(best)