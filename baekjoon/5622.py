def str2sec(getstr):
	charAtdial = ['','',"ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
	total = 0
	for x in getstr:
		for y in range(10):
			if x in charAtdial[y]:
				total += 1+y
	return total

print(str2sec(input()))