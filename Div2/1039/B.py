# from collections import defaultdict
from collections import deque
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        nums = deque(map(int, input().split()))

        asc = True
        traceback = []
        while len(nums) >= 2:
            left = nums.popleft()
            right = nums.pop()
            # left, right = nums[0], nums[-1]
            
            if left < right:
                if asc:
                    traceback += ["L", "R"]
                else:
                    traceback += ["R", "L"]
            elif right < left:
                if asc:
                    traceback += ["R", "L"]
                else:
                    traceback += ["L", "R"]
            asc = not asc
        if len(nums) == 1:
            traceback.append("L")
        
        print(''.join(traceback))