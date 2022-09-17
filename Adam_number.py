n=int(input())
sqn=n*n
revn=int(str(n)[::-1])
revsqn=revn*revn
print(sqn==int(str(revsqn)[::-1]))