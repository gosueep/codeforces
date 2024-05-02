# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        nums = list(map(int, input().split()))
        # nums.sort()
        # nums[-2] += 1
        
        best = -1
        for i in range(len(nums)):
            out = 1
            for j in range(len(nums)):
                if i == j: out *= (nums[j]+1)
                else: out *= nums[j]
            best = max(out, best)
        print(best)                