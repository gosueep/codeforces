if __name__ == '__main__':
    cases = int(input())

    for _ in range(cases):
        n = int(input())
        hps = list(map(int, input().split()))
        spells = list(map(int, input().split()))

        time = sum(hps)
        time += sum(spells) - max(spells)

        print(time)


