# from collections import defaultdict

def onetwo():
    N = int(input())
    nums = list(map(int, input().split()))

    left = [0 for i in range(N)]
    right = [0 for i in range(N)]

    prod = 1
    for i, x in enumerate(nums[:-1]):
        prod *= x
        left[i] = prod

    prod = 1
    for i, x in enumerate(reversed(nums[1:])):
        prod *= x
        right[N-i-2] = prod

    # print(left, right)

    for i in range(0, N-1):
        if left[i] == right[i]:
            return i+1
    
    return -1


if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        print(onetwo())
