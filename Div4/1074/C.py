# from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        arr = list(map(int, input().split()))
        arr = list(sorted(set((arr)))) # why does set place negatives at the end???
        # print('AHH  ', arr)
        mex = 1
        curr = 1
        for i in range(len(arr)-1):
            if arr[i]+1 == arr[i+1]:
                curr+=1
            else:
                mex = max(mex, curr)
                curr = 1
        print(max(mex,curr))