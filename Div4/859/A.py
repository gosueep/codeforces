# from collections import defaultdict

if __name__ == '__main__':
    cases = int(input())

    for _ in range(cases):
        a, b, c = map(int, input().split())
        
        one = (a + b) == c
        two = (a - b) == c
        
        if one:
            print('+')
        else:
            print('-')