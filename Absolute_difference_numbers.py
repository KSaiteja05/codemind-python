m,x=map(int,input().split())
n=str(m)
f=''
l=''
for i in range(x):
    f+=n[i]
for i in range(len(str(n))-1,len(str(n))-1-x,-1):
    l+=n[i]
l=(l)[::-1]
print(abs(int(f)-int(l)))