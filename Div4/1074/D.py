# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N,M,memMax = map(int, input().split())
        orig = list(map(int, input().split()))
        ops = [map(int,input().split()) for _ in range(M)]
        trans = [0 for _ in range(N)]
        versions = [0 for _ in range(N)]
        curr_version = 0

        for i,c in ops:
            i = i-1
            if versions[i] != curr_version:
                trans[i] = 0
                versions[i] = curr_version

            trans[i] += c
            newVal = orig[i] + trans[i]
            if newVal > memMax:
                curr_version += 1
        for i in range(N):
            if versions[i] != curr_version:
                trans[i] = 0
                
        print(' '.join([str(orig[i]+trans[i]) for i in range(N)]))