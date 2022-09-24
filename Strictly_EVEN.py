n=int(input())
cnt=c=0
l=list(map(int,input().split()))
for i in range(0,len(l),2):
    if(i%2==0 and l[i]%2==0):
        cnt+=1
for i in range(len(l)):
    if(l[i]%2==0):
        c+=1
print(cnt==c)    