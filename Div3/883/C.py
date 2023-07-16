# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N, probs, mins = map(int, input().split())
        
        scores = []
        for person in range(N):
            times = list(map(int, input().split()))
            times.sort()
            # print(times)
            solves = 0
            time = 0
            penalty = 0
            for i in times:
                time += i
                if time > mins:
                    break
                solves += 1
                penalty += time
            scores.append((solves, penalty))
        
        rudolph = scores[0]
        # print(rudolph)
        # print(scores)
        place = 1
        best = (0, 0)
        scores.sort(key=lambda x: (x[0], -x[1]), reverse=True)
        # print(scores)
        for solves, pen in scores:
            if solves > rudolph[0]:
                place += 1
            elif solves == rudolph[0]:
                if pen < rudolph[1]:
                    place += 1
                else:
                    break
        print(place)
        
        
        