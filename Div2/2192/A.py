# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        s = input().strip()

        blocks = [1]
        for i in range(1,N):
            if s[i-1] == s[i]:
                blocks[-1] += 1
            else:
                blocks.append(1)
        
        # print(s, blocks)
        if len(blocks) > 1:
            if s[0] == s[-1]:
                blocks[0] += blocks.pop()
        # print(blocks)
        score = len(blocks)
        if len(blocks) > 1 and any([block > 1 for block in blocks]):
            score += 1
        print(score)
