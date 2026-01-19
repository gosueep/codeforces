# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N, c = map(int , input().split())
        nums = list(map(int, input().split()))
        nums.sort(reverse=True)

        cost = 0

        while len(nums) != 0:
            new_nums = []
            for x in nums:
                if x > c:
                    cost += 1
                else:
                    new_nums.append(x)
            if len(new_nums) > 0:
                new_nums.pop(0)
                new_nums = [x*2 for x in new_nums]
            nums = new_nums

        print(cost)