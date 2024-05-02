# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        i = 0
        ppl = input().strip()
        if 'A' not in ppl:
            print(0)
        else:
            while ppl[i] == 'P':
                i += 1
            # print(i, ppl[i:])
            ppl = ppl[i:].split('A')
            print(max(len(i)for i in ppl))
            # print(ppl)