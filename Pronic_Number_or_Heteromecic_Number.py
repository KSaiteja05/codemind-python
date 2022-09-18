n=int(input())
y=0
for i  in range(1,n):
    if(i*(i+1)==n):
        y=1
if(y==1):
    print("YES")
else:
    print("NO")