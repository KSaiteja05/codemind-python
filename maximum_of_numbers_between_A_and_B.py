n=int(input())
l=list(map(int,input().split()))
cnt=0
max=0
a,b=map(int,input().split())
for i in range(len(l)):
    if(l[i]>=a and l[i]<=b):
        if(l[i]>max):
            max=l[i]
if(max==0):
    print(-1)
else:
    print(max)