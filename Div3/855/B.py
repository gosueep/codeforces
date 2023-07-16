

if __name__ == '__main__':
    cases = int(input())

    for _ in range(cases):
        n, k = map(int, input().split())
        s = input()
            
        letters = [[0, 0] for _ in range(26)]

        for c in s:
            pos = ord(c.lower()) - ord('a')
            letters[pos][c.isupper()] += 1
        
        total = 0
        changed = 0
        for low, up in letters:
            total += min(low, up)
            changed += abs(low - up) // 2
        print(total + min(changed, k))
