n=input()
n=n.lower()
s=set(n)
x=list(s)
x.sort()
for i in range(len(x)):
    if(x[i]!=' '):
        print(x[i],end='')