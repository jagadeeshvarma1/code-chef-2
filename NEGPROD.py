
for _  in  range(int(input())):
    a=list(map(int,input().split()))
    o=0
    p=0
    for i in a:
        if i>0:
            o+=1
        elif i<0:
            p+=1
    if o>=1 and p>=1:
        print("yes")
    else:print("no")    