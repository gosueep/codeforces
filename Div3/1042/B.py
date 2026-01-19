# from collections import defaultdict
from collections import deque
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        array = []
        for i in range(N):
            if i % 2 == 0:
                array.append('-1')
            else:
                array.append('3')
        if array[-1] == '3':
            array[-1] = '2'
        print(' '.join(array))