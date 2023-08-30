t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if(x>0 and y>0):
        print("Solution")
    elif(x>0):
        print("Solid")
    else:
        print("Liquid")