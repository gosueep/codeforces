from collections import defaultdict

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        a = map(int, input().split())

        counts = defaultdict(int)
        for i in a:
            counts[i] += 1
        s = sorted(counts, reverse=True)

        result = []
        while counts:
            for i in s:
                if counts[i] > 0:
                    result.append(i)
                    counts[i] -= 1
                else:
                    counts.pop(i)

        ugly = False
        curr_sum = 0
        for i in result:
            if i == curr_sum:
                ugly = True
            else:
                curr_sum += i

        if ugly:
            print('NO')
        else:
            print('YES')
            print(' '.join(map(str, result)))
