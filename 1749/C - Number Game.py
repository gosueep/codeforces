if __name__ == '__main__':
    cases = int(input())

    for _ in range(cases):
        n = int(input())
        nums = list(map(int, input().split()))
        nums.sort()

        stage = 0
        i = 0
        print(nums)
        while i < n:
            if stage+1 >= nums[i]:
                stage += 1
                i += 2
            else:
                break

        print(stage)
