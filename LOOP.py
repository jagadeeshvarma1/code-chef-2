for _ in range(int(input())):
    a,b,m=map(int,input().split())
    x=(a-b)%m
    y=(b-a)%m
    
    print(min(x,y))