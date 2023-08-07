# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N, k = map(int, input().split())
        health = list(map(int, input().split()))
        
        hits = []
        for i in range(N):
            hp = health[i] % k
            if hp == 0:
                hp = k
            hits.append((-hp, i+1))
        
        # print(k)
        # print(health)
        # print(hits)
        hits.sort()
        # print(hits)
        
        print(' '.join(str(x[1]) for x in hits))
        