l=list(map(str,input().split()))
v=['a','e','i','o','u','A','E','I','O','U']
cnt=0
for i in range(len(l)):
    s=l[i]
    if(s[0] in v and s[len(s)-1] not in v):
        cnt+=1
print(cnt)