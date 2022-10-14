n=int(input())
m=q=n
while(n):
    prime=True
    for i in range(2,int(n**(0.5)+1)):
        if(n%i==0):
            prime=False
    if(prime==True):
        x=n
        break
    else:
        n+=1
while(m):
    prime=True
    for i in range(2,int(m**(0.5)+1)):
        if(m%i==0):
            prime=False
    if(prime==True):
        y=m
        break
    else:
        m-=1
if(x-q<q-y):
    print(x-q)
else:
    print(q-y)