# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N,M,k = map(int, input().split())
        robots = list(map(int, input().split()))
        spikes = set(map(int, input().split()))
        instructions = input().strip()

        shift = 0
        alive = set(robots)
        live_bots = []
        for x in instructions:
            if x == 'L':
                shift -= 1
            if x == 'R':
                shift += 1
            
            for bot in list(alive):
                if bot + shift in spikes:
                    alive.remove(bot)
            live_bots.append(len(alive))
        
        print(' '.join([str(x) for x in live_bots]))
