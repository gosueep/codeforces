# from collections import defaultdict

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):

        N = int(input())
        nums = list(map(int, input().split()))

        pos = []
        neg = []

        smallest = 10e10
        for i in nums:

            if abs(i) < smallest:
                smallest = abs(i)

            if i > 0:
                pos.append(i)
            else:
                neg.append(i*-1)

        if len(neg) % 2 == 0:
            print(sum(pos) + sum(neg))
        else:
            print(sum(pos) + sum(neg) - smallest*2)