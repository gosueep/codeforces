# from collections import defaultdict

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        
        q = []
        for _ in range(N-1):
            a, b = map(int, input().split())
            q.append((a, b))
        
        drawn = set([1])
        reads = 1
        # while len(drawn) < N:
        for src, dest in q:
            # if src in drawn:
            #     drawn.add(dest)
            # if dest in drawn:
            if src in drawn and dest in drawn:
                reads += 1
            drawn.add(src)
            drawn.add(dest)
                
        print(reads)
        
