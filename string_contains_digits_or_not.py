for i in range(int(input())):
    n=input()
    p=0
    l=['1','2','3','4','5','6','7','8','9','0']
    for j in range(len(n)):
        if(n[j] in l):
            p=1
            break
    if(p==1):
        print("Yes")
    else:
        print("No")