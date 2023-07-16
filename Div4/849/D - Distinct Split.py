# from collections import defaultdict

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):

        N = int(input())
        s = input()

        counts = [0 for x in range(N-1)]
        l = set()
        r = set()
        # i is split, left is string from [0 : i], inclusive, right is [i+1 : N] inclusive
        for i, x in enumerate(s[:-1]):
            l.add(x)
            counts[i] += len(l)
        for i, x in enumerate(reversed(s[1:])):
            r.add(x)
            counts[N-2 -i] += len(r)

        print(max(counts))
