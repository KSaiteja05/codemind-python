a=int(input())
b=int(input())
for i in range(a,b+1):
    x=i
    cnt=0
    if "0" in str(x):
        continue
    else:
        while(i):
            m=i%10
            if(x%m==0):
                cnt+=1
            i//=10
    if(len(str(x))==cnt):
        print(x,end=' ')