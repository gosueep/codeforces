# from collections import defaultdict

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())
        nums = list(map(int, input().split()))
        
        parity = [0,0]
        minodd = int(1e9) + 1
        mineven = int(1e9) + 1
        for i in nums:
            if i % 2 == 1:
                minodd = min(minodd, i)
                parity[1] += 1
            else:
                mineven = min(mineven, i)
                parity[0] += 1
        
        # if all even or all odd or can make every even odd w/o being negative
        # print(mineven, minodd)
        if parity[0] == 0 or parity[1] == 0 or mineven-minodd > 0:
            print('YES')
        else:
            print('NO')
            
        
