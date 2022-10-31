n=input()
p=-1
for i in range(len(n)):
    if(n.count(n[i])==1):
        p=n[i]
        break
print(p)