# from collections import defaultdict

def digitsum(n):
    x = 0
    while n > 0:
        x += n % 10
        n = n // 10
    return x


def twosum():
    N = int(input())

    l, r = 0, N

    while l < r:
        x = (l + r) // 2
        y = N - x

        dx, dy = digitsum(x), digitsum(y)

        if abs(dx - dy) <= 1:
            break
        elif dx > dy:
            r = x
        else:
            l = x

    print(x, y)
    # print(digitsum(x), digitsum(y))



if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        twosum()
