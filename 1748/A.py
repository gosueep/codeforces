import math


if __name__ == '__main__':
    cases = int(input())

    for _ in range(cases):
        n = int(input())

        div = math.ceil(n / 2)
        squares = div * (div+1)
        if n % 2 == 1:
            squares -= div

        maxBlocks = math.floor(squares ** 0.5)

        print(maxBlocks)