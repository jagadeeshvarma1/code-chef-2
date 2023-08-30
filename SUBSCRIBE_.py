for t in range(int(input())):
    n, x = map(int, input().split())
    if n > 6:
        if n%6 == 0:
            a = n/6
            print(int(x*a))
        else:
            b = n//6
            b = b+1
            print(int(x*b))
    else:
        print(x)
    