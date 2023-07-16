for _ in range(int(input())):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    s = 0
    evens = 0
    odds = 0
    for i in arr:
        s += i
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1

    for i in range(q):
        eo, add = map(int, input().split())
        if eo == 0:
            s += add * evens
            if add % 2 == 1:
                odds += evens
                evens = 0
        else:
            s += add * odds
            if add % 2 == 1:
                evens += odds
                odds = 0
        print(s)