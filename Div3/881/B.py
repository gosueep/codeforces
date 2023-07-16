# from collections import defaultdict

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        A = list(map(int, input().split()))

        ops = 0
        total = 0
        inOp = False
        for i in A:
            if i == 0:
                continue
            total += abs(i)
            if i <= 0:
                if not inOp:
                    ops += 1
                    inOp = True
            else:
                inOp = False
        print(total, ops)