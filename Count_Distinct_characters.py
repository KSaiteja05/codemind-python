n=input()
n=n.lower()
s=set(n)
x=list(s)
cnt=0
for i in range(len(x)):
    if(x[i]!=' '):
        cnt+=1
print(cnt)