# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        n = int(input())
        nums = list(map(int, input().split()))

        total = 0
        last = nums[0]
        currlen = 1
        for x in nums[1:]:
            if last == x:
                continue
            if last + 1 == x:
                currlen += 1
            else:
                total += (currlen+1) //2
                currlen = 1
            last = x
        
        total += (currlen+1)//2
        print(total)
            