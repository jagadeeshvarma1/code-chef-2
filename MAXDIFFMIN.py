# cook your dish here
t=int(input())
for i in range(t):
    a=list(map(int,input().split()))
    for j in a:
        print(max(a)-min(a))
        break