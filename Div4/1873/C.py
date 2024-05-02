# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        target = []
        for i in range(10):
            target.append(input().strip())
        
        N=10
        score = 0
        for i in range(N):
            for j in range(N):
                if target[i][j] == 'X':
                    temp = min(min(i, 9-(i)),min(j, 9-(j)))+1
                    score += temp
                    # print(temp)
        print(score)