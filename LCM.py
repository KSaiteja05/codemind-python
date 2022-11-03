a,b=map(int,input().split())
x=a
y=b
while(a!=0 and b!=0):
    if(a>b):
        a-=b
    else:
        b-=a
if(b==0):
    gcd=a
else:
    gcd=b
lcm=(x*y)//gcd
print(lcm)