# from collections import defaultdict
import sys

if __name__ == '__main__':
    cases = int(input())

    for _ in range(cases):
        N = int(input())
        A = list(map(int, input().split()))
        
        up, u = [0]*N, 0
        for i in range(N):
            u += A[i]
            up[i] = u
            
        l, r = 1, N+1
        while l <= r:
            k = (l+r) // 2
            
            print(f'? {k}', end=' ')
            for x in range(1, k+1):
                print(x, end=' ')
            print()
            sys.stdout.flush()
            
            # sys.stdout.flush()
            # _ = input()
            total = int(input())
            
            # expected = up[k-1] - up[l-1]
            expected = up[k-1]
            
            # print(expected, total)
            
            if expected < total:
                r = k-1
            elif expected == total:
                l = k+1
            # print('\t', l, r, k)
        print(f'! {k}')
        sys.stdout.flush()
                