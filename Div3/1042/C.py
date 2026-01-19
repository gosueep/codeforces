# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N,k = map(int,input().split())
        start = map(int,input().split())
        target = map(int,input().split())

        start_dict = {}
        # target_dict = {}
        for i in range(k):
            start_dict[i] = 0
            # target_dict[i] = 0
        for i in start:
            mod = i % k
            key = min(k-mod, mod)
            start_dict[key] += 1
        for i in target:
            mod = i % k
            key = min(k-mod, mod)
            start_dict[key] += 1
        

        # print(start_dict)
        # print(target_dict)

        if all(x == 0 for x in start_dict.values())
            print('YES')
        else:
            print('NO')
                
