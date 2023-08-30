for t in range(int(input())):
    a, b, c = map(int, input().split())
    if a != b:
        if a != c and b != c:
            print("yes")
        else:
            print("no")
    else:
        print("no")