t=int(input())
for _ in range(t):
    a,x,b,y=map(int,input().split())
    if(a/x > b/y):
        print("Alice")
    elif(a/x < b/y):
        print("Bob")
    else:
        print("Equal")