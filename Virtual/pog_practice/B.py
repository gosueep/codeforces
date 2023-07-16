# from collections import defaultdict

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        nums = list(set(map(int, input().split())))
        
        neg = 0
        big = -1
        for i in nums:
            big = max(i, big)
            if i < 0:
                neg = i
                break
        
        if neg == 0:
            print(big)
        else:
            print(neg)