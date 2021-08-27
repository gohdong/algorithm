test_case = int(input())
ar = []
for x in range(test_case):
	a = input()
	this_score = 1
	total = 0
	for x in a:
		if x =='O':
			total += this_score
			this_score +=1
		else:
			this_score = 1

	ar.append(total)

for x in range(test_case):
	print(ar[x])


