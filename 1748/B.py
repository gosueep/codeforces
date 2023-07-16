import math


if __name__ == '__main__':
    cases = int(input())

    for _ in range(cases):
        length = int(input())
        s = input()

        distinct = 0
        for winLen in range(1, length+1):
            print(winLen, s[:winLen])
            seen = set(s[:winLen])
            start, stop = 0, winLen
            while stop < length:
                print(seen)
                if len(seen) >= winLen:
                    distinct += 1
                seen.remove(s[start])
                start += 1
                stop += 1
                seen.add(s[stop-1])

        print(distinct)
        print()