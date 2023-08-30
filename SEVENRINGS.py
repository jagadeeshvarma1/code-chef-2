t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if 9999<x*y<100000:
        print("YES")
    else:
        print("NO")