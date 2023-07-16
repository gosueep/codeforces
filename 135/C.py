
def findMin(arr, value):

    for i in range(len(arr)):
        if arr[i] >= value:
            if i == 0:
                return arr[0]
            return arr[i-1]
    return arr[i]

    l = 0
    r = len(arr)-1
    i = int((l + r) / 2)
    while r > l:
        # print(l, r, i)

        if arr[i] >= value:
            r = i-1

        elif arr[i] < value:
            l = i+1

        i = int((l + r) / 2)



    return arr[i]

def findMax(arr, value):

    for i, val in enumerate(reversed(arr)):
        print(val)
        if val <= value:
            if i == 0:
                return val
            return arr[i-1]
    # return arr[-1]

def minmax():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # for i in range(n):
    #     print(findMin(b, a[i]) - a[i], end=' ')
    # print()
    for i in range(n):
        print(findMax(b, a[i] - a[i]), end=' ')

    print()
    return


if __name__ == "__main__":
    cases = int(input())
    for _ in range(cases):
        minmax()