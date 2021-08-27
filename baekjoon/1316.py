def check_group_voca(getstr):
	used_char = []	
	if len(getstr)==0:
		return True
	for x in range(1,len(getstr)):
		if getstr[x] not in used_char:
			if getstr[x] != getstr[x-1]:
				used_char.append(getstr[x-1])
		else:
			return False

	return True



n = input()
count = 0
for i in range(int(n)):
	getstr = input()
	if check_group_voca(getstr) == True:
		count +=1

print(count)

