# from collections import defaultdict

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):

        N = int(input())
        A = map(int, input().split())
        
        curr = 0
        longest = 0
        for i in A:
            if i == 0:
                curr += 1
                if curr > longest:
                    longest = curr
            else:
                curr = 0
            
            
        print(longest)