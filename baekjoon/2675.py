a = int(input())
b = []

for i in range(a):
	c,d = input().split()
	e = ""
	for x in d:
		for k in range(int(c)):
			e=e+x
	b.append(e)

for j in range(a):
	print(b[j])