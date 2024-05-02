# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        arr = list(map(int, input().split()))
        
        rems = [0,0,0]
        
        for i in arr:
            arr[i%3] += 1
        
        avg = sum(rems)//3
        
        moves = 0
        for i in rems:
            moves += abs(avg-i)
        
        print(moves)
        