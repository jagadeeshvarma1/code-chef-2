for t in range(int(input())):
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    if a+b == c or b+c == a or c+a == b:
        print("yes")
    else:
        print("no")