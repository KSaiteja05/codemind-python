n=input()
l=['a','e','i','o','u']
p=0
for i in range(len(l)):
    if(l[i] in n):
        continue
    else:
        print(l[i],end=' ')
        p=1
if(p==0):
    print(0)