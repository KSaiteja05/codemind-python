def isprime(n):
    if n==0:
        return 0
    else:
        for i in range(2,n//2):
            if(n%i==0):
                return 0
    return 1
def fisprime(n):
    while(n!=0):
        n+=1
        if(isprime(n)==1):
            return n
def lisprime(n):
    while(n!=0):
        n-=1
        if(isprime(n)==1):
            return n
n=int(input())
if(isprime(n)==1):
    print(0)
else:
    x=fisprime(n)
    y=lisprime(n)
    x=x-n
    y=n-y
    print(min(x,y))