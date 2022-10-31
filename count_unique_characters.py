n=input()
n=n.lower()
s=set(n)
x=list(s)
cnt=0
for i in range(len(x)):
    if(n.count(x[i])==1 and x[i]!=' '):
        cnt+=1
print(cnt)