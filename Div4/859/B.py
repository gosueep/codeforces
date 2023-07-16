# from collections import defaultdict

if __name__ == '__main__':
    cases = int(input())

    for _ in range(cases):
        n = int(input())
        A = map(int, input().split())
        
        even, odd = 0, 0
        for i in A:
            if i % 2 == 0:
                even += i
            else:
                odd += i
        
        if even > odd:
            print('YES')
        else:
            print('NO')