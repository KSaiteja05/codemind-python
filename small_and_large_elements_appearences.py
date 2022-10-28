n=input()
n=n.replace(' ','')
def unimx(n):
    mx=max(n)
    return(mx)
def unimn(n):
    mn=min(n)
    return(mn)
mx=mn=0
x=unimn(n)
y=unimx(n)
c1=n.count(x)
c2=n.count(y)
print(x,c1,y,c2)