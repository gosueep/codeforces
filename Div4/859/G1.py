# from collections import defaultdict
import sys


if __name__ == '__main__':
    cases = int(input())

    for _ in range(cases):
        N = int(input())
        target = list(map(int, input().split()))
        target.sort()
        
        curr, total = set([1]), 1
        # print(curr, total)
        
        possible = True
        
        if target[0] != 1:
            possible = False
        else:
            for i in target[1:]:
                # print(target, curr, total)
                if i > total:
                    possible = False
                    # print('not possible')
                    break
                curr.add(i)
                total += i
        
        if possible:
            print('YES')
        else:
            print('NO')
        
