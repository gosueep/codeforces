

if __name__ == '__main__':
    cases = int(input())

    for _ in range(cases):
        s = input()

        if s[:6] in 'YesYesYes':
            print('YES')
        else:
            print('NO')
