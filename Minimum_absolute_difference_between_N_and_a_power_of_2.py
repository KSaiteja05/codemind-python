n=int(input())
i=0
while(n!=0):
    if(2**i<=n):
        x=2**i
    if(2**i>=n):
        y=2**i
        break
    i+=1
print(min(n-x,y-n))