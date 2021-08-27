a = input()
count = 0
for x in a:
	if x == ' ':
		count+=1
b = a.strip().split(' ')
if count == len(a):
	print(0)
else:
	print(len(b))