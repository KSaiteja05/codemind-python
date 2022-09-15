n=int(input())
s=str(n)
e=0
o=0
for i in range(len(s)):
    if(int(s[i])%2==0):
        e+=1
    elif(int(s[i])%2==1):
        o+=1
if(e==len(s)):
    print("Even")
elif(o==len(s)):
    print("Odd")
else:
    print("Mixed")