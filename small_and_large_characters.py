n=list(map(str,input().split()))
def unimx(n):
    mx=max(n)
    return(mx)
def unimn(n):
    mn=min(n)
    return(mn)
mx=mn=0
for i in range(len(n)):
    x=unimx(n[i])
    y=unimn(n[i])
    print(y,x,end=' ')