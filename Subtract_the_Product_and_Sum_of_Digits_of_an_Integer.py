n=int(input())
s=str(n)
p=1
sum=0
for i in range(len(s)):
    p=p*int(s[i])
    sum=sum+int(s[i])
print(abs(p-sum))