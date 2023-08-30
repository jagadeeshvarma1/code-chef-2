for t in range(int(input())):
    n, x = map(int, input().split())
    a = n*x
    if a%4 == 0:
        print(int(a/4))
    else:
        print(a//4+1)