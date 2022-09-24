n=int(input())
l=list(map(int,input().split()))
cnt=0
min=10
a,b=map(int,input().split())
for i in range(len(l)):
    if(l[i]>=a and l[i]<=b):
        if(l[i]<min):
            min=l[i]
if(min==10):
    print(-1)
else:
    print(min)