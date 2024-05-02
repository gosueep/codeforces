# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        num = input().strip()
        l=len(num)
        num = int(num)
        out = (l-1) * 9
        
        i = 1
        while True:
            if int(str(i)*l) > num:
                break
            out += 1
            i += 1
        
        # print(l, small)
        print(out)

        