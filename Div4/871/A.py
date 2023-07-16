# from collections import defaultdict

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):

        origin = 'codeforces'
        N = len(origin)

        s = input()
        
        diff = 0
        for i in range(N):
            if s[i] != origin[i]:
                diff += 1
            
        print(diff)