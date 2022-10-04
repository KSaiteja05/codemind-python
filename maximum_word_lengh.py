n=input()
l=res=0
for i in range(len(n)):
    if(n[i]!=" "):
        l+=1
    else:
        res=max(res,l)
        l=0
print(max(res,l))