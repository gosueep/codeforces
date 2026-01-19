# from collections import defaultdict
import sys
import copy
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N,M,k = map(int, input().split())
        robots = list(map(int, input().split()))
        spikes = list(map(int, input().split()))
        instructions = input()

        # get ranges for bots
        
        bot_lefts = [-1 for _ in range(N)]
        bot_rights = [-1 for _ in range(N)] # boo clanker rights
        curr_left_spike = -1
        last_bot_index = -1

        r, s = 0,0
        while r < N and s < M:
            bot = robots[r]
            spike = spikes[s]

            if bot < spike:
                bot_lefts[r] = curr_left_spike
                last_bot_index = r
                r += 1
            else:
                curr_left_spike = spike
                i = last_bot_index
                while i > 0 and bot_rights[i] != -1:
                    bot_rights[i] = spike
                    i -= 1
                s += 1

        max_left = 0
        max_right = 0
        curr_pos = 0
        live_bots = []
        for x in instructions:
            if x == 'L':
                curr_pos -=1
            if x == 'R':
                curr_pos += 1
            
            alive = 0
            for i in range(N):
                pos = robots[i]
                if bot_lefts[i] < pos + max_left and pos + max_right < bot_rights[i]:
                    alive += 1
            live_bots.append(alive)
        

        print(bot_lefts, bot_rights)
        print([str(x) for x in live_bots])

        # # find max left and max right from instructions
        # max_left = 0
        # max_right = 0
        # curr = 0
        # for x in instructions:
        #     if x == 'L':
        #         curr -=1
        #     if x == 'R':
        #         curr += 1
        #     max_left = min(max_left, curr)
        #     max_right = max(max_right, curr)
        
        # alive = 0
        # for i in range(N):
        #     pos = robots[i]
        #     if bot_lefts[i] < pos + max_left and pos + max_right < bot_rights[i]:
        #         alive += 1

        # print(alive)