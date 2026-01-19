from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        adj = defaultdict(list)
        for _ in range(N-1):
            u,v = map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        
        # choose the last as the root (i think it doesn't matter)
        q = [u]
        seen = set()
        leaves = 0
        i = 0
        while len(q) > 0:
            i += 1
            next = []
            for x in q:
                if x not in seen:
                    seen.add(x)
                    leaf = True
                    for v in adj[x]:
                        if v not in seen:
                            next.append(v)
                            leaf = False
                    
                    if leaf and i > 1:
                        leaves += 1
            q = next
        
        print(leaves//2)

        

        
            
            


                
