# from collections import defaultdict

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        n,k,x = map(int, input().split())
        
               
        possible = False
        # if 1 allowed, use all 1's
        if x != 1:
            taken = [1 for x in range(n)]
            possible=True
        else:
            # if only 2 allowed, and n is not even, skip - not possible
            if not (k == 2 and n%2!=0) and not (k == 1):  
                # else, either all 2's or 1 3 and all 2's
                possible = True
                taken = [2 for x in range(n//2 - 1)]
                if n%2==0:
                    taken.append(2)
                else:
                    taken.append(3)
                
                
        if possible:
            print('YES')
            print(len(taken))
            [print(i, end=" ") for i in taken]
            print()
        else:
            print('NO')