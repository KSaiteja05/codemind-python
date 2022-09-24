x,y=map(int,input().split())
cnt=0
n=set(map(int,input().split()))
m=set(map(int,input().split()))
s1=list(n)
s2=list(m)
for i in range(len(s1)):
    if(s1[i] not in s2):
        cnt+=1
for i in range(len(s2)):
    if(s2[i] not in s1):
        cnt+=1
print(cnt)