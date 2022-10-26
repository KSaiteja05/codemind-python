l=list(map(str,input()))
l1=list(map(str,input()))
l.extend(l1)
l.sort()
for i in range(len(l)):
    print(l[i],end='')