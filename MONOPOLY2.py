for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    print('YES' if a+b+d<c or a+b+c<d or a+c+d<b or b+c+d<a else 'NO')