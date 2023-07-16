cases = int(input())

IMG_SIZE = 2

for _ in range(cases):
    colors = set()

    for i in range(IMG_SIZE):
        for pixel in input():
            colors.add(pixel)

    print(len(colors)-1)
