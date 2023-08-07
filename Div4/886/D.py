# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N, k = map(int, input().split())
        probs = list(map(int, input().split()))

        probs.sort()
        start = 0
        longest = -1
        for i in range(1, N):
            if probs[i] - probs[i-1] > k:
                setlen = i - start
                longest = max(longest, setlen)
                start = i
        longest = max(longest, N-start)
        print(N-longest)        