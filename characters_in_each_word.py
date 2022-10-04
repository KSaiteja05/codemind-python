n=input()
l=0
for i in range(len(n)):
    if(n[i]!=" "):
        l+=1
    else:
        print(l,end=' ')
        l=0
print(l)