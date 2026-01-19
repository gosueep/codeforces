# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        A = list(map(int,input().split()))
        B = list(map(int,input().split()))

        # total = 1
        # for a,b in zip(A,B):
        #     if a>b:
        #         total += a-b

        maxdiff = sum([A[i] - B[i] for i in range(N) if A[i] > B[i]])+1
        print(maxdiff)
