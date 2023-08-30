for _ in range(int(input())):
    n=int(input())
    m=list(map(int,input().split()))
    count=0
    for i in m:
        if(i>=10 and i<=60):
            count+=1
    print(count)