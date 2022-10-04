n=input()
le=input()
p=0
print(le in n)
for i in range(len(n)):
    if(le==n[i]):
        print(i)
        p=1
        break
if(p==0 and le in n):
    print('False')