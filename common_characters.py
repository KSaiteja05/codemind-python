a=input()
b=input()
a=a.lower()
b=b.lower()
l=[]
p=-1
for i in range(len(a)):
    if(a[i] in b and a[i]!=' '):
        l.append(a[i])
        p=1
s=set(l)
l=list(s)
l.sort()
if(p==1):
    for i in range(len(l)):
        print(l[i],end='')
else:
    print(p)