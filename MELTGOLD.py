import math
T=int(input())
for _ in range(T):
    X,Y=map(int,input().split())
    z=2*(X-Y)
    print(round(math.sqrt(z)))