n=input()
l=['a','e','i','o','u','A','E','I','O','U']
p=cnt=0
for i in range(len(n)):
    if(n[i] in l):
        cnt+=1
        p=1
if(p==0):
    print(0)
else:
    print(cnt)