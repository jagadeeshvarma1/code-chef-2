for _ in range(int(input())):
    x,y,z=map(int,input().split())
    a=x*y
    b=x+z
    print(min(a,b))