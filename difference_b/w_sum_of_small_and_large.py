n=list(map(str,input().split()))
def unimx(n):
    mx=max(n)
    return(ord(mx))
def unimn(n):
    mn=min(n)
    return(ord(mn))
mx=mn=0
for i in range(len(n)):
    mx+=unimx(n[i])
    mn+=unimn(n[i])
print(mx-mn)