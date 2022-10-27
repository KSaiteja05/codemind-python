n=input()
l=['a','e','i','o','u']
num=['1','2','3','4','5','6','7','8','9','0']
v=c=nu=w=0
for i in range(len(n)):
    if(n[i] in l):
        v+=1
    if(n[i] not in l and n[i]!=' ' and n[i] not in num):
        c+=1
    if(n[i] in num):
        nu+=1
    if(n[i] == ' '):
        w+=1
print("Vowels: {}".format(v))
print("Consonants: {}".format(c))
print("Digits: {}".format(nu))
print("White spaces: {}".format(w))