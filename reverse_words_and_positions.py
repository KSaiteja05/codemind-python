l=list(map(str,input().split()))
for i in range(len(l)-1,0-1,-1):
    s=l[i]
    print(s[::-1],end=' ')