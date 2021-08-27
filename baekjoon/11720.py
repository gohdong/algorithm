a = int(input())
b = int(input())
sum =0
aaa = list()
for i in range(0,a):
	aaa.append(b//(10**(a-1-i)))
	b -= aaa[i]*(10**(a-1-i))
	sum += aaa[i]

print(sum)
