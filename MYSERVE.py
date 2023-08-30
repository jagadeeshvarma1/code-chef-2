for i in range(int(input())):
    p,q=map(int,input().split())
    z=p+q
    if(z%4==1 or z%4==0):
        print("Alice")
    else:
        print("Bob")