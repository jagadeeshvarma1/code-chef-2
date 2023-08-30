for _ in range(int(input())):
    n=int(input())
    x=n%10
    if x>=5:
        print(100-(10*(n//10+1)))
    else:
        print(100-(10*(n//10)))