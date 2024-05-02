# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    As = 0
    Bs = 0
    inp = input().strip()
    out = []
    ops = 0
    for i in range(2, N+1, 2):
        sub = inp[i-2:i]
        if sub in ['aa', 'bb']:
            out.append('ab')
            ops += 1
        else:
            out.append(sub)
    
    print(ops)
    print(''.join(out))

    
    