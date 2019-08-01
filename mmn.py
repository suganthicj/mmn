    
x11=int(input())
l=list(map(int,input().split(" ")))
z11=l[0]
for p in range(0,len(l)):
	y11=z11&l[p]
print(y11)
