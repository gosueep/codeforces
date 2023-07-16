# from collections import defaultdict


if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):

        n, m = map(int, input().split())
        s = list(input())
        t = list(input())

        both = s + [x for x in reversed(t)]

        doubled = 0
        i = 1
        while i < len(both):
            if both[i] == both[i-1]:
                doubled += 1
            i += 1
        
        # print(both, doubled)
        
        if doubled > 1:
            print('NO')
        else:
            print('YES')



