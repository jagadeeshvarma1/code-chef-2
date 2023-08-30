for t in range(int(input())):
    x, y, z = map(int, input().split())
    if x > y and x > z:
        print("Setter")
    elif y > x  and y > z:
        print("tester")
    else:
        print("editorialist")