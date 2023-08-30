# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    m=max(a)
    while m in a:
        a.remove(m)
    n=max(a)
    print(m+n)
            
        