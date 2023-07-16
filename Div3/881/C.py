# from collections import defaultdict
 
if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
 
        i = N
        total = 0
        while i > 0:
            total += i
            i = i // 2
        print(total)