# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        A = list(map(int, input().split()))
        
        
        coins = 0
        two = False
        one = False
        zero = False
        for i in A:
            if i == 0:
                coins += 1
                if one or two:
                    
                else:
                    zero = True
                    
                    
            if two:
                if i != 0:
                    continue
                else:
                    two = False
            
            elif zero:
                if i == 1:
                    continue
                elif i == 2:
                    two = True
                else:
                    coins += 1
                    zero = True

                
            
        