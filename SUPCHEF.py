for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if((y*z)<x):
        print("Yes")
    else:
        print("No")
        