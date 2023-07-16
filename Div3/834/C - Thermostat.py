

def thermostat(low, high, x, init, final):
    diff = abs(final - init)
    maxUp_f = high - final
    maxDown_f = final - low
    maxUp_i = high - init
    maxDown_i = init - low

    if init == final:
        return 0
    elif diff >= x:
        return 1
    else:
        if maxUp_f >= x:
            if maxUp_i >= x:
                return 2
            elif maxDown_i >= x:
                return 3
        elif maxDown_f >= x:
            if maxDown_i >= x:
                return 2
            elif maxUp_i >= x:
                return 3
    return -1


if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        low, high, x = map(int, input().split())
        init, final = map(int, input().split())

        print(thermostat(low, high, x, init, final))


