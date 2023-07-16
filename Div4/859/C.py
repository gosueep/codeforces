# from collections import defaultdict

def alt(string):
    zero = set()
    one = set()

    z = True
    string = input()
    for s in string:
        if z:
            if s in one:
                return False
            if s not in zero:
                zero.add(s)
        else:
            if s in zero:
                return False
            if s not in one:
                one.add(s)
        
        z = not z
    
    return True


if __name__ == '__main__':
    cases = int(input())

    for _ in range(cases):
        if alt(input()):
            print('YES')
        else:
            print('NO')