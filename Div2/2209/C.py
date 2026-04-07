from collections import defaultdict
import sys
input = sys.stdin.readline


def query(i,j) -> bool:
    print(f"? {i} {j}")
    sys.stdout.flush()
    ans = int(input())
    if ans == -1:
        exit()
        return True
    if ans == 1:
        print(f"! {i}")
        sys.stdout.flush()
        return True
    return False

if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        N = int(input())

        won = False

        # leave first pair -> n-1 queries (leaves 2 queries)
        for i in range(3,2*N+1,2):
            j = i+1
            won = query(i,j)
            if won: break

        # if we've gone through every pair and they weren't 00, that means every pair must have had 0X
        # first pair was untouched - choose first num in first pair and compare with 2nd pair
        # query 1,3 and 1,4
        # IF first pair is 0X - one query will return 1, so we found a zero
        # IF 2nd   pair is X0 - both will return 0, so 2 must be a zero
        if not won:
            for i,j in [(1,3), (1,4)]:
                won = query(i,j)
                if won: break
            if not won:
                print(f"! 2")
                sys.stdout.flush()
