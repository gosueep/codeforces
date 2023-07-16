# from collections import defaultdict

from math import log, ceil


class RMQ:
    def __init__(self, n):
        self.inf = float("inf")
        self.low, self.high = 0, n - 1
        self.sz = pow(2, int(ceil(log(n, 2))))
        self.dat = [self.inf] * (2 * self.sz - 1)

    def build(self, arr):
        return self.build_help(arr, self.low, self.high, 0)

    def build_help(self, arr, low, high, pos):
        if low == high:
            self.dat[pos] = arr[low]
            return
        mid = (low + high) / 2
        self.build_help(arr, low, mid, 2 * pos + 1)
        self.build_help(arr, mid + 1, high, 2 * pos + 2)
        self.dat[pos] = self.dat[2 * pos + 1] + self.dat[2 * pos + 2]

    def update(self, idx, val):
        self.update_help(idx, self.low, self.high, 0, val)

    def update_help(self, idx, low, high, pos, val):
        if idx < low or idx > high:
            return
        if low == high:
            self.dat[pos] = val
            return
        mid = (low + high) / 2
        self.update_help(idx, low, mid, 2 * pos + 1, val)
        self.update_help(idx, mid + 1, high, 2 * pos + 2, val)
        self.dat[pos] = self.dat[2 * pos + 1] + self.dat[2 * pos + 2]

    def query(self, qlow, qhigh):
        return self.query_help(qlow, qhigh, 0, self.high, 0)

    def query_help(self, qlow, qhigh, low, high, pos):
        if qlow <= low and qhigh >= high:  # TOTAL OVERLAP
            return self.dat[pos]
        if qlow > high or qhigh < low:  # NO OVERLAP
            return 0
        mid = (low + high) / 2
        # PARTIAL OVERLAP
        return self.query_help(qlow, qhigh, low, mid, 2 * pos + 1) + self.query_help(qlow, qhigh, mid + 1, high,
                                                                                     2 * pos + 2)


if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N, Q = map(int, input().split())
        # arr = list(map(int, input().split()))
        arr = [0] * N

        rmq = RMQ(N)
        rmq.build(arr)
        for i in range(Q):
            query = input()
            if query[0] == "F":
                instr, num = query.split()
                rmq.update(num-1)
            else:
                instr, low, high = query.split()
                amt = rmq.query(low, high)
                print(amt)
                