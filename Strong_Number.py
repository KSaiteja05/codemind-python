import math
def isdiv(n):
    s=0
    x=n
    while(n>0):
        r=n%10
        s+=math.factorial(r)
        n=n//10
    if(x==s):
        return True
    else:
        return False
n=int(input())
if(isdiv(n)==1):
    print("The number {} is a strong number".format(n))
else:
    print("The number {} is not a strong number".format(n))