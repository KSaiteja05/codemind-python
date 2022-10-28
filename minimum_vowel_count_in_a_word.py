n=list(map(str,input().split()))
l=['a','e','i','o','u']
m=1000
cnt=0
for i in range(len(n)):
    s=n[i]
    for j in range(len(s)):
        if(s[j] in l):
            cnt+=1
    m=min(m,cnt)
    cnt=0
print(m)