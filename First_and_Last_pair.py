n=int(input())
l=list(map(int,input().split()))
cnt=0
for i in range(len(l)):
    if(len(l)%2==1 and cnt==(len(l))//2):
        print(l[i],end=' ')
        break
    elif(cnt==(len(l))//2):
        break
    print(l[i],l[len(l)-(i+1)],end=' ')
    cnt+=1
if(len(l)%2==1):
    print(0)