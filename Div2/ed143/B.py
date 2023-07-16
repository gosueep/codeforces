# from collections import defaultdict


if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):

        n, k = map(int, input().split())

        points = [0 for x in range(51)]
        for _ in range(n):
            start, end = map(int, input().split())
            if start <= k <= end:
                for i in range(start, end+1):
                    points[i] += 1

        ideal = True
        for i, x in enumerate(points):
            if i != k and x >= points[k]:
                ideal = False

        if ideal:
            print('YES')
        else:
            print('NO')




