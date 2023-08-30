# cook your dish here
t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    if (2*y) >= (3*x):
        print(3*x)
    else:
        print(2*y)