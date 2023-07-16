# from collections import defaultdict


if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):

        n = int(input())
        teas = list(map(int, input().split()))
        tasters = list(map(int, input().split()))
        drank = [0 for _ in range(n)]

        for i in range(n):
            for j in range(i, n):
                if teas[j-i] > 0:
                    amt = min(teas[j-i], tasters[j])
                    drank[j] += amt
                    teas[j-i] -= amt

        print(' '.join([str(x) for x in drank]))





