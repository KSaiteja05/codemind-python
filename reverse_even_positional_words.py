l=list(map(str,input().split()))
for i in range(len(l)):
    if(i%2==0):
        s=l[i]
        print(s[::-1],end=' ')
    else:
        print(l[i],end=' ')