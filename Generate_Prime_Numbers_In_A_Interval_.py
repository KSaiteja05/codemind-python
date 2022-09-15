def isprime(n):
    cnt=0
    for i in range(1,n+1):
        if(n%i==0):
            cnt+=1
    if(cnt==2):
        return True
    else:
        return False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(isprime(i)==True):
        print(i)