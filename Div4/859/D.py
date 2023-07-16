# from collections import defaultdict

if __name__ == '__main__':
    cases = int(input())

    for _ in range(cases):
        N, Q = map(int, input().split())
        A = list(map(int, input().split()))
        
        up, total = [0]*N, 0
        for i in range(N):
            total += A[i] % 2
            up[i] = total
        
        output = []
        for q in range(Q):
            l, r, k = map(int, input().split())
            
            left = 0 if l == 1 else up[l-2]
            right = up[r-1]
            
            res = total - (right - left) + ((r-l+1)%2) * (k%2)

            if res % 2 == 1: 
                # print('YES')
                output.append('YES')
            else:
                # print('NO')
                output.append('NO')
            
        print('\n'.join(output))
            
        