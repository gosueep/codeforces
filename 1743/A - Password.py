import math


if __name__ == '__main__':
    cases = int(input())

    for _ in range(cases):
        numNotUsed = int(input())
        nums = input()

        print(math.comb(10 - numNotUsed, 2) * 6)
