# from collections import defaultdict
import heapq

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):

        N, M = map(int, input().split())
        prep = map(int, input().split())
        wins = [0 for x in range(N+1)]

        # Player 0 is you
        for i, x in enumerate(sorted(prep)):
            if x <= M:
                wins[0] += 1
                M -= x
            else:
                wins[i+1] += 1

        print(N, wins, (N) * (N-1) // 2)

        games_left = N * (N-1) // 2
        for x in wins[1:]:
            if x < wins[0]:
                games_left -= wins[0] - x
        print(games_left)


        # Each opponent has n-2 games to play
        # # (n-1) * (n-2) / 2    games left if n players in total
        # # n * n-1 // 2 since N = num opps = players - 1
        # pq = []
        # for i, x in enumerate(wins[1:]):
        #     heapq.heappush(pq, (x, i+1))
        # for _ in range(N * (N-1) // 2):
        #     score, player = heapq.heappop(pq)
        #     heapq.heappush(pq, (score+1, player))
        #     wins[player] += 1
        #
        # print(wins)


