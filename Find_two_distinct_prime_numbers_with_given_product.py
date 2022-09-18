def isprime(n):
    cnt=0
    for i in range(1,n+1):
        if(n%i==0):
            cnt+=1
    if(cnt==2):
        return 1
    else:
        return 0
n=int(input())
x=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if(isprime(i)==1 and isprime(j) and i*j==n):
            print(i,j)
            x=1
            break
    if(x==1):
        break
if(x==0):
    print(-1)