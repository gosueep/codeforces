from collections import defaultdict

cases = int(input())
for _ in range(cases):
    n, k = map(int, input().split())
    s = input()
    t = input()

    convertible = True

    if sorted(s) != sorted(t):
        convertible = False
    elif n < 2*k:
        if n <= k:
            if s != t:
                convertible = False
        else:
            convertible = s[n-k:k] == t[n-k:k]

    
    if convertible:
        print('YES')
    else:
        print('NO')
