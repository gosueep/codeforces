

if __name__ == '__main__':
    cases = int(input())

    for _ in range(cases):
        n = int(input())
        s = input().lower()
            
        cut = s[0]
        for i in range(1, n):
            c = s[i]
            if c != cut[-1]:
                cut += c
        # print(cut)
        if cut == 'meow':
            print('YES')
        else:
            print('NO')

