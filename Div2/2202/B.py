import heapq
from collections import deque
import sys
input = sys.stdin.readline


# ts so wrong - can calculate in linear time bud
if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N, active, win_con, max_cost = map(int, input().strip().split())
        costs = list(map(int, input().strip().split()))
        index_to_cost = {i: costs[i] for i in range(N)}

        last_cycle_cost = -1 # last cost playing win_con
        curr_cycle_cost = 0 # curr cost of playing win_con
        total_cost = 0
        times_win_con_played = 0

        #priority queue - index, sorted by cost, active hand
        hand = []
        # queue of nums - deck
        deck = deque()

        win_con_in_hand = False
        for i, c in enumerate(costs):
            if i < active:
                heapq.heappush(hand, (c, i))
                if i == win_con:
                    win_con_in_hand = True
            else:
                deck.append((c,i))
        
        while total_cost < max_cost:
            print(hand, deck)
            if win_con_in_hand:
                times_win_con_played += 1

                # if played before and cycle cost is the same, assume we're in a cycle (is this okay?)
                if last_cycle_cost != -1 and last_cycle_cost == curr_cycle_cost:
                    cycles_left = (max_cost - total_cost) // curr_cycle_cost
                    total_cost += cycles_left * curr_cycle_cost
                    times_win_con_played += cycles_left
                    total_cost = max_cost # set to max to break
                else:
                    win_con_in_hand = False
                    # remove from heap manually
                    i = hand.index((index_to_cost[win_con], win_con))
                    hand.pop((i,win_con))
                    heapq.heapify(hand)

                
                last_cycle_cost = curr_cycle_cost
                curr_cycle_cost = 0
            else:
                i, c = heapq.heappop(hand)

            total_cost += c
            curr_cycle_cost += c
            deck.append((c,i))
            heapq.heappush(hand, deck.popleft())
            if i == win_con:
                win_con_in_hand = True

        
        print(times_win_con_played)


