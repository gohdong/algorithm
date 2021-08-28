a = int(input())
b = int(input())
c = int(input())

d = a*b*c

count = [0,0,0,0,0,0,0,0,0,0]


for x in str(d):
	count[int(x)]+=1

for x in range(0,10):
	print(count[x])