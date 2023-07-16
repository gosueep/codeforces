from collections import deque

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        
        N, M = map(int, input().split())
        
        grid = []
        for i in range(N):
            grid.append(list(map(int, input().split())))
            
        q = deque()
        maxdepth = 0
        seen = set()
        for i in range(N):
            for j in range(M):
                depth = grid[i][j]
                if (i,j) not in seen and depth != 0:
                    seen.add((i,j))
                    curr = deque([(i,j)])
                    while curr:
                        ci, cj = curr.popleft()
                        for newi, newj in [(ci,cj+1), (ci,cj-1), (ci+1,cj), (ci-1,cj)]:
                            if 0 <= newi < N and 0 <= newj < M and (newi,newj) not in seen:
                                seen.add((newi,newj))
                                if grid[newi][newj] != 0:
                                    curr.append((newi,newj))
                                    depth += grid[newi][newj]
                    maxdepth = max(maxdepth, depth)
            
        print(maxdepth)