
if __name__ == '__main__':

    permSums = {}
    for n in range(1, 101):
        permSums[(n * (n + 1) // 2)] = n

    cases = int(input())

    for _ in range(cases):
        numFound, sumLost = map(int, input().split())
        nums = list(map(int, input().split()))

        maxN = max(nums)
        total = sum(nums) + sumLost

        if total in permSums and maxN <= permSums[total]:
            print('YES')
        else:
            print('NO')
