m=int(input())
x=len(str(m))
s=0
n=m*m
while(x>0):
    r=n%10
    s=s*10+r
    n=n//10
    x-=1
if(m==int(str(s)[::-1])):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')