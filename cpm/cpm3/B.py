from collections import deque
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort(reverse=True)
    arr = deque(arr)
    print(arr)

    l = []
    r = []
    
    for i in range(N):
        if i%2 == 0:
            l.append(arr[i])
        else:
            r.append(arr[i])
            
    
    nums = 0
    for i in range(1,N-1):
        if out[i-1] < out[i] and out[i] > out[i+1]:
            nums += 1
    
    print(nums)
    print(' '.join([str(x) for x in out]))
        
    
    