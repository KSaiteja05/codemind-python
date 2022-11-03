n=input()
s=0
j=1
for i in range(len(n)):
    s+=int(n[i])**j
    j+=1
print(s==int(n))