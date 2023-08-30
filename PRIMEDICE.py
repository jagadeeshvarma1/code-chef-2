prime=[1,2,3,5,7,11,13]
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    add=a+b
    if add in prime:
        print("Alice")
    else:
        print("Bob")