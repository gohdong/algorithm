a,b = input().split()
c = []
c.append(input().split())
d = c[0]

for x in range(0,int(a)):
	if(int(d[x])<int(b)):
		print(d[x],end=' ')