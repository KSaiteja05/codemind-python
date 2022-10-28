s=input()
su=0
n=['1','2','3','4','5','6','7','8','9','0']
for i in range(len(s)):
    if(s[i] in n):
        su+=int(s[i])
print(su)