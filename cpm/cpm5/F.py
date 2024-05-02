from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    out = []
    
    cases = int(input())
    for _ in range(cases):
        N = int(input())

        arr = list(map(int, input().split()))
        arr.sort()
        
        print(arr)
        
        amt = 0
        i = N-1
        while i > 0:
            exp = arr[i]
            if exp == 1 or i - exp < 0:
                break
            i = i-exp+1
            amt += 1
        
        print(i)
        amt += i+1
            

        out.append(str(amt))
    print('\n'.join(out))