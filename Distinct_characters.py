n=input()
n=n.lower()
l=[]
for i in range(len(n)):
    if(n.count(n[i])==1 and n[i]!=' '):
        l.append(n[i])
l.sort()
for i in range(len(l)):
    print(l[i],end='')