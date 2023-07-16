

if __name__ == '__main__':
    cases = int(input())

    for _ in range(cases):
        n = int(input())
        s = input()

        unique = 1
        for i in range(2, n):
            if s[i] != s[i-2]:
                unique += 1

        print(unique)
    