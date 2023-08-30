# cook your dish here
exam=int(input())
for e in range(exam):
  A,B,C= map(int,input().split())
  total = A+B+C
  if total >= 100 and (A>=10 and B>=10 and C>=10):print("pass")
  else:print("fail")