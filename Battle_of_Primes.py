a=int(input())
b=int(input())
def isprime(n):
    if(n<=1):
        return 0
    for i in range(2,n):
        if(n%i==0):
            return 0
    return 1
n=a+b
c=i=1
while(n):
    if(isprime(n+i)==1):
        break
    else:
        c+=1
        i+=1
print(c)