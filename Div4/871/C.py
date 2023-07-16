# from collections import defaultdict

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):

        N = int(input())
        min1, min2 = int(1e6), int(1e6)
        minboth = int(1e6)
        for i in range(N):
            mins, skill = input().split()
            mins = int(mins)
            
            if skill == '01':
                if mins < min1:
                    min1 = mins
            elif skill == '10':
                if mins < min2:
                    min2 = mins
            elif skill == '11':
                if mins < minboth:
                    minboth = mins
        
        best = min1 + min2
        best = min(best, minboth)
        if best >= int(1e6):
            best = -1
            
        print(best)