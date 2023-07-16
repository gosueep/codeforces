# from collections import defaultdict

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        A = list(map(int, input().split()))
        A.sort()
        
        l, r = 0, N-1
        
        total = 0
        while l < r:
            total += A[r] - A[l]
            l += 1
            r -= 1

        print(total)