# from collections import defaultdict

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):

        N = int(input())
        s = input()

        i = 0
        while i < N-1 - i and s[i] != s[N-1 - i]:
            i += 1
        print(N-1 - i - i + 1)