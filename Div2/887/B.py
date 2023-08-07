# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N, length = map(int, input().split())
    
        seq = 0
        for i in range(N//2, N+1):
            curr, b = i, N-i
            if curr < b:
                continue
            # print(N, curr, end=', ')
            # print(curr, b, end=', ')
            
            a = curr - b
            k = 3
            while a <= b:
                # print(b,a, end=', ')
                k += 1
                b, a = a, b-a
            # print()
            # print(k)
            if k >= length:
                seq += 1
        print(seq)
        
        # break
                
            