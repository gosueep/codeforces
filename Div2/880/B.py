from collections import defaultdict

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N, k, g = map(int, input().split())
        
        if g % 2 == 0:
            half = (g // 2) - 1
        else:
            half = g // 2
        
        
        saved = 0
        if half * N >= k * g:
            saved = k*g
        else:
            i = int(half * N / g)
            # while g * i / N <= half:
            #     i += 1
            saved = g * (i)
        print(saved)
