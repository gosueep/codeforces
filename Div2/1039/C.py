# from collections import defaultdict
# from collections import deque
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        nums = list(map(int, input().split()))

        possible = True
        smallest = nums[0]
        for i in range(1,N):
            if nums[i] > smallest and nums[i] - smallest > smallest:
                possible = False
                break

            if nums[i] < smallest:
                smallest = nums[i] 

        print('yes' if possible else 'no')
                
