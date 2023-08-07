from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        points = []
        
        for i in range(N):
            x, y = map(int, input().split())
            points.append((x,y))
        
        vert = defaultdict(int)
        hor = defaultdict(int)
        pos = defaultdict(int)
        neg = defaultdict(int)
        
        total = 0
        for i in range(N):
            x, y = points[i]
            total += vert[x] * 2
            vert[x] += 1
            
            total += hor[y] *2
            hor[y] += 1
            
            total += pos[y-x]*2
            pos[y-x]+=1
            
            total += neg[y+x]*2
            neg[y+x]+=1
        
        # print(vert, hor, pos, neg)
            
        print(total)
                
                
        