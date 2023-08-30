for _ in range(int(input())):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    count= 0
    for i in range(n):
        if a[i] >= x:
            count += b[i]
    print(count)