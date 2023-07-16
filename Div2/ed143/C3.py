# from collections import defaultdict


if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):

        n = int(input())
        teas = list(map(int, input().split()))
        tasters = list(map(int, input().split()))
        drank = [0 for _ in range(n)]

        for i, x in enumerate(teas):

            while i < n and x > 0:
                amt = min(x, tasters[i])
                x -= amt
                drank[i] += amt
                i += 1

        print(' '.join([str(x) for x in drank]))


