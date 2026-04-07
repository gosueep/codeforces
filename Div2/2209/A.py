from collections import defaultdict
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N, c, flip_flops = map(int, input().strip().split())
        monsters = list(map(int, input().strip().split()))

        monsters.sort()
        strength = c
        for power in monsters:
            if strength >= power:
                diff = strength - power
                ff_to_use = min(diff, flip_flops)
                flip_flops -= ff_to_use
                strength += power + ff_to_use
            else:
                break
        
        print(strength)