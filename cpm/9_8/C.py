# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    counts = [[0,0]]*26
    for _ in range(N):
        c = int(ord(input()[0]) - ord('a'))
        a,b = counts[c]
        
        if a > b:
            b += 1
        else:
            a += 1
        counts[c] = [a,b]
    
    result = 0
    for a,b in counts:
        if a > 1:
            result += a*(a-1)//2
        if b > 1:
            result += b*(b-1)//2
            
    print(result)
        
        