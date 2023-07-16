from collections import defaultdict

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        n = int(input())
        a = list(map(int, input().split()))

        counts = defaultdict(int)
        for i in a:
            counts[i] += 1

        print(a)
        print(counts)

        s = set(range(1,n+1))
        needed = set()
        p = [-1 for x in range(n)]
        q = [-1 for x in range(n)]
        for i, x in enumerate(a):
            if counts[x] == 1:
                p[i] = x
                q[i] = x
                s.remove(x)
            else:
                needed.add(x)

        #     if x in s:
        #         needed.add(x)
        #         q[i] = x
        #     else:
        #         p[i] = x
        #         s.add(x)
        # print(a)
        print(p)
        print(q)
        print(s)
        # print(needed)
        #
        # if len(needed) == 0:
        #     print('YES')
        #     print(' '.join(map(str, p)))
        #     print(' '.join(map(str, p)))

        print()

# 5 3 4 2 5
# 5 3 4 2 1
# x 3 4 2 5
