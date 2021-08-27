count = 0
n = int(input())

for x in range(1,n+1):
	if x==1000:
		continue
	elif x<100:
		count +=1
	else:
		a = int(x/100)
		b = int((x-a*100)/10)
		c = x- a*100 - b*10
		if(b-a == c-b):
			count+=1

print(count)

