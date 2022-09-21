def isprime(n):
    if(n<=1): 
        return 0
    for i in range(2,n//2+1):
        if(n%i==0):
            return 0
    return 1
def isdigprime(n):
    while(n!=0):
        r=n%10
        if(isprime(r)==0):
            return 0
        n=n//10
    return 1
n=int(input())
if(isprime(n)==1 and isdigprime(n)==1):
    print('Mega Prime')
else:
    print('Not Mega Prime')