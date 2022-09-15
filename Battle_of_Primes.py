def isprime(s):
    cnt=0
    for i in range(1,s+1):
        if(s%i==0):
            cnt+=1
    if(cnt==2):
        return True
    else:
        return False
f=int(input())
l=int(input())
s=f+l
c=0
if(isprime(s)==True):
    s+=1
    c+=1
while(s):
    if(isprime(s)==True):
        break
    else:
        s+=1
    c+=1
print(c)