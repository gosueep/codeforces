from collections import defaultdict

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        robots = list(map(int, input().split()))

        counts = defaultdict(int)
        for i in robots:
            counts[i] += 1
        
        consistent = True
        for i in range(1, 100):
            if counts[i] > counts[i-1]:
                consistent = False
                break
        
        if consistent:
            print("YES")
        else:
            print("NO")