def isprime(n):
    cnt=0
    for i in range(1,n+1):
        if(n%i==0):
            cnt+=1
    if(cnt==2):
        return True
    else:
        return False
n=int(input())
if(isprime(n)==1 and isprime(int(str(n)[::-1]))==1):
    print("circular prime")
elif(isprime(n)==1):
    print("prime but not a circular prime")
else:
    print('not prime')