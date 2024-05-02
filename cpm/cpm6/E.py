# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    
    subs = 0
    while True:
        # print("N", N)
        if N == 0 or N==1:
            break
        if N % 2 == 0:
            subs += N//2
            break
        
        i = 3
        while i**2 <= N:
            if N%i == 0:
                break
        subs += 1
        N = N//i
        
    print(subs)
        

        