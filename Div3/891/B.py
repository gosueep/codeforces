# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        num = [int(i) for i in input().strip()]
        N = len(num)
        rounded = False
        carry = 0
        i = N-1
        highest = N
        while i >= 0:
            if num[i] + carry >= 5:
                rounded = True
                carry = 1
                highest = i-1
            else:
                carry = 0
            i -= 1
        # print(num, rounded, highest, num[min(0, highest)])
        
        if rounded:
            if highest == -1:
                print(10 ** N)
            else:
                i = N-highest-1
                base = 10**(i)
                x = num[highest] * base
                x += base
                # print(N, highest, x, i)
                # print(x)
                
                for i in reversed(num[:highest]):
                    base *= 10
                    x += base * i
                print(x)
        else:
            print(''.join(str(i) for i in num))