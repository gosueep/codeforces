
if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        n, k = map(int, input().split())
        perm = list(map(int, input().split()))

        num_sorted = 1
        start = 1
        for i in range(perm.index(1), n-1):
            if start+1 == perm[i+1]:
                start += 1
                num_sorted += 1

        # print(perm)
        # print(num_sorted, n - num_sorted)
        print(-((n - num_sorted) // -k))
        # print()

