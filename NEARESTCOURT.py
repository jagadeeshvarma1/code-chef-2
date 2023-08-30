# cook your dish here
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    m=(a+b)//2
    x=abs(m-a)
    y=abs(m-b)
    print(max(x,y))