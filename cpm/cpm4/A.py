# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, k = map(int, input().split())

    # d, c, nw = 0,0,0
    
    # c = k*d
    # d+c = d + k*d = d(k+1)
    # w = d+c-nw <= n/2
    
    # w = d(k+1) -nw <= n/2
    
    # nw = N//2
    
    half = N//2
    d = half // (k+1)
    print(d, k*d, N-d*(k+1))
        
        
        