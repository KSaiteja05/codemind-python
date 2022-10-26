n=input()
p=0
x=-1
for i in range(len(n)):
    if(n.count(n[i])==1):
        p=1
        x=i
        break
if(p==1):
    print(x)
else:
    print(x)