# from collections import defaultdict
import sys

def div3(N):
    return N % 3 == 0


if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        
        N, M = map(int, input().split())
        
        seen = set()
        def gold(N):
            if N < M:
                return
            
            seen.add(N)
            if N == M:
                return
            
            if N not in seen:
                if div3(N):
                    gold(N//3*2)
                    gold(N//3)

        gold(N)

        if M in seen:
            print('YES')
        else:
            print('NO')