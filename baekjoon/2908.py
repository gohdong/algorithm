def find_bigger(a,b):
	if a>=b:
		return a
	else:
		return b


a = input().split()
a[0] = int(a[0][::-1])
a[1] = int(a[1][::-1])

print(find_bigger(a[0],a[1]))