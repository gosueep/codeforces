# from collections import defaultdict
import sys
input = sys.stdin.readline


# you can paint the repaint ANY color - might need to redo soln

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N, k = map(int, input().split())
        bridge = list(map(int, input().split()))
        
        indices = [[-1] for x in range(k)]
        for i in range(N):
            c = bridge[i]
            indices[c-1].append(i)

        for i in range(k):
            indices[i].append(N)
            
        hops = []
        for c in range(k):
            color = indices[c]
            best = [0, 0]
            i = 1
            while i < len(color):
                planks = color[i]-color[i-1]-1
                if planks > best[0]:
                    best = [planks, best[0]]
                elif planks > best[1]:
                    best[1] = max(best[1], planks)
                i += 1
            hops.append(max(best[0]//2, best[1]))
        
        # print(hops)
        minstep = min(hops)
        print(minstep)
            