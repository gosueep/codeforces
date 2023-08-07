# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N, k = map(int, input().split())
        days = list(map(int, input().split()))
        
        setlen = days[-1]
        day = days[-1]+1
        
        curr = [x+1 for x in range(setlen)]
        saved = []
        days = set(days)
        for i in range(1,day):
            if i not in days:
                saved.append(i)
        

        # print(curr, day)
        while len(curr) < setlen:
            curr.append(day)
            day += 1
        print(days)
        print(saved)
        print(curr, day)
        
        for i in range(k-1):
            newday = []
            for s in saved:
                newday.append(curr[s])
            curr = newday
            while len(curr) < setlen:
                curr.append(day)
                day += 1
            print(curr)
        print(curr)
        print(curr[0])
        print()
                
                
            