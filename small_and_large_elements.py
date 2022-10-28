l=list(map(str,input().split()))
def unimx(n):
    mx=max(n)
    return(mx)
def unimn(n):
    mn=min(n)
    return(mn)
mx=mn=0
x=l[0]
y=l[len(l)-1]
print(unimn(x),unimx(y))