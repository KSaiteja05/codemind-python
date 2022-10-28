n=list(map(str,input().split()))
def unimx(n):
    mx=max(n)
    return(ord(mx))
def unimn(n):
    mn=min(n)
    return(ord(mn))
mx=mn=0
for i in range(len(n)):
    x=unimx(n[i])
    y=unimn(n[i])
    print(x-y,end=' ')