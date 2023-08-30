test=int(input())

for item in range(test):
    math1,math2=map(int,input().split())
    if (math1 >= math2):
        print('0')
    else:
        print(math2-math1)