if __name__ == '__main__':
    cases = int(input())

    for _ in range(cases):
        n = int(input())

        perm = [1]

        i = n
        while i > 1:
            perm.append(i)
            i -= 1

        for i in perm:
            print(i, end=' ')
        print()

