# from collections import defaultdict

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N, L, H = map(int, input().split())
        bases = list(map(int, input().split()))
        
        bases.sort()
        halflen = L/2
        area = L*H*N    # undivided
        invslope = halflen/H
        # print('inv', invslope, L, H)
        for i in range(N-1):
            top = bases[i] + H
            if top > bases[i+1]:
                overlap = top - bases[i+1]
                x = invslope * (bases[i+1]-bases[i])
                newl = halflen-x
                area -= newl * 2 * overlap
                # print('overlap', overlap, newl)
                # print('minus', newl * 2 * overlap)
        # print(area)
        print(area/2)
        
        
        