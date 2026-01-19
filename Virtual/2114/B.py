# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        n,k = map(int, input().split())
        s = input().strip()
        ones = 0
        zeros = 0
        for c in s:
            if c == '0':
                zeros += 1
            elif c == '1':
                ones += 1
        nonpairs = n//2 - k
        ones -= nonpairs
        zeros -= nonpairs
        if ones < 0 or zeros < 0:
            print("NO")
        else:                
            if ones %2 ==0 and zeros %2 == 0:
                print("YES")
            else:
                print("NO")