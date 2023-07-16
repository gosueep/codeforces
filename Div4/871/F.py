import sys
sys.setrecursionlimit(2 ** 30)


# class UnionFind:
#     def __init__(self, N,M):
#         self.p = []          # parent list
#         for i in range(N):
#             row = []
#             for j in range(M):
#                 row.append((i,j))
#             self.p.append(row)
#         self.numSets = N*M
#         # self.N = N*M

#     # join two sets
#     def union(self, a, b):
#         a = self.find_set(a)
#         b = self.find_set(b)
#         if a != b:
#         #     if self.sizes[a] < self.sizes[b]:
#         #         self.p[a] = self.p[b]
#         #         self.sizes[b] += self.sizes[a]
#         #     else:
#         #         self.p[b] = self.p[a]
#         #         self.sizes[a] += self.sizes[b]
#             self.p[a] = self.p[b]
#             self.numSets -= 1

#     # Find set of given int v
#     def find_set(self, v):
#         if v == self.p[v]:
#             return v
#         self.p[v] = self.find_set(self.p[v])
#         return self.p[v]
    
class UnionFind:
    def __init__(self, N):
        self.p = [x for x in range(N)]          # parent list
        self.rank = []                          # Not implemented
        self.sizes = [1 for x in range(N)]
        self.N = N

    # join two sets
    def union(self, a, b):
        a = self.find_set(self.p[a])
        b = self.find_set(self.p[b])
        if a != b:
            if self.sizes[a] < self.sizes[b]:
                self.p[a] = self.p[b]
                self.sizes[b] += self.sizes[a]
            else:
                self.p[b] = self.p[a]
                self.sizes[a] += self.sizes[b]

    # Find set of given int v
    def find_set(self, v):
        if v == self.p[v]:
            return v
        self.p[v] = self.find_set(self.p[v])
        return self.p[v]


if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        
        N, M = map(int, input().split())
        ufds = UnionFind(N*M)
        
        grid = []
        for i in range(N):
            grid.append(list(map(int, input().split())))
        
        for i in range(N):
            for j in range(M):
                for newi, newj in [(i,j+1), (i,j-1), (i+1,j), (i-1,j)]:
                    if 0 <= newi < N and 0 <= newj < M:
                        if grid[i][j] !=0 and grid[newi][newj] != 0:
                            src = i*N + j
                            dest = newi*N + j
                            ufds.union(src, dest)

        print(max(ufds.sizes))
