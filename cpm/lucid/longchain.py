from collections import defaultdict, deque
n = int(input())

adjList = defaultdict(set)
animals = set()
for _ in range(n):
    pred, preys = input().split('<-')
    pred = pred.strip()
    animals.add(pred)
    for prey in preys.split(','):
        prey = prey.strip()
        adjList[pred].add(prey)
        animals.add(prey)
        
# long = -1
# seen = set()
# for a in animals:
#     if a not in seen:
#         dfs = deque([(a, 1)])
#         while dfs:
#             curr, l = dfs.pop()
#             seen.add((curr, l))
#             long = max(long, l)
#             for p in adjList:
#                 if (p,l) not in seen:
#                     dfs.append((p, l+1))
            
# print(long)

memo = {}
def chain(x):    
    if x in memo:
        return memo[x]
    if x not in adjList:
        return 1
    
    cs = []
    for p in adjList[x]:
        cs.append(1 + chain(p))
    memo[x] = max(cs)
    return memo[x]
        
chains = []
for a in animals:
    chains.append(chain(a))
print(max(chains))