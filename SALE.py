for _ in range(int(input())):
    x,y,z=map(int,input().split())
    print(x+y+z-min(x,y,z))