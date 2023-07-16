import heapq

if __name__ == '__main__':
    cases = int(input())

    for _ in range(cases):
        n = int(input())
        cards = list(map(int, input().split()))

        total = 0
        bonuses = []

        for i in cards:
            if i == 0:
                if bonuses:
                    power = heapq.heappop(bonuses)
                    total += -power
            else:
                heapq.heappush(bonuses, -i)

        print(total)