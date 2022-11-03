n=int(input())
def isprime(n):
    if(n<=1):
        return 0
    for i in range(2,n):
        if(n%i==0):
            return 0
    return 1
if(isprime(n)==1 and isprime(int(str(n)[::-1]))==1):
    print("circular prime")
elif(isprime(n)==1):
    print("prime but not a circular prime")
else:
    print("not prime")