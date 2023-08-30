T = int(input())
for i in range(T):
    a,c = map(int,input().split())
    sol= (a+c)/2
    print(int(sol)) if sol%1==0 else print(-1)