n=input()
l=['a','e','i','o','u']
cnt=0
for i in range(len(l)):
    if(l[i] in n):
        cnt+=1
print(cnt==len(l))