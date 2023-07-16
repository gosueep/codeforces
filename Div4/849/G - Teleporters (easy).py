# from collections import defaultdict

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):

        N, C = map(int, input().split())
        costs = list(map(int, input().split()))
        for i, x in enumerate(costs):
            costs[i] += i+1

        s = sorted(costs)
        used = 0
        for i in s:
            if i <= C:
                used += 1
                C -= i
            else:
                break
        print(used)
