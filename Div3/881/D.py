from collections import defaultdict

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        adjlist = defaultdict(list)
        for _ in range(N-1):
            u, v = map(int, input().split())
            adjlist[u].append(v)
            adjlist[v].append(u)
        
        leaves = [0 for x in range(N+1)]
        parent = [0 for x in range(N+1)]
        dfs = [1]
        seen = set()
        while dfs:
            curr = dfs.pop()
            seen.add(curr)
            leaf = True
            for i in adjlist[curr]:
                if i not in seen:
                    dfs.append(i)
                    parent[i] = curr
                    leaf = False
            
            if leaf:
                leaves[curr] = 1
            #     numleaves[curr] = 1
            #     p = parent[curr]
            #     while p != 0:
            #         numleaves[p] += 1
            #         p = parent[p]
        # print(parent)
        # print(numleaves)
        
        def count(a):
            if leaves[a] != 0:
                return leaves[a]
            num = 0
            for i in adjlist[a]:
                if i != parent[a]:
                    num += count(i)
            leaves[a] = num
            return num
        Q = int(input())
        for _ in range(Q):
            a, b = map(int, input().split())
            print(count(a) * count(b))