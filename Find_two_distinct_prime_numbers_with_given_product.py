n=int(input())
def isprime(n):
    if(n<=1):
        return 0
    for i in range(2,n):
        if(n%i==0):
            return 0
    return 1
p=-1
for i in range(n):
    for j in range(n):
        if(i*j==n and isprime(i)==1 and isprime(j)==1):
            p=1
            x=i
            y=j
            break
print(y,x) if p==1 else print(p)