for i in range(int(input())):
    n=input()
    x=n[::-1]
    if(n==x):
        if(len(n)%2==0):
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")