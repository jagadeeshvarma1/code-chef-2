for t in range(int(input())):
    n, x, k = input().split()
    n, x, k = int(n), int(x), int(k)
    if n * x <= k:
        print("yes")
    else:
        print("no")