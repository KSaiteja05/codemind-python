l=list(map(str,input().split()))
def vow(l):
    v=['a','e','i','o','u','A','E','I','O','U']
    x=len(l)-1
    cnt=0
    for i in range(len(l)):
        if((l[i] in v and l[x] not in v and l[i]!=' ' and l[x]!=' ') or (l[i] not in v and l[x] in v and l[i]!=' ' and l[x]!=' ')):
            cnt+=1
        x-=1
    return(cnt//2)
cnt=0
for i in range(len(l)):
    cnt+=vow(l[i])
print(cnt)