def count_char(getstr):
	getstr = getstr+'  '
	count = len(getstr)
	for x in range(count):
		if len(getstr.strip()) >= 3:
			if getstr[x] == '=' or getstr[x] == '-':
				count -= 1
			if getstr[x] == 'd' and getstr[x+1] =='z' and getstr[x+2] == '=':
				count -= 1

			if getstr[x] == 'l' and getstr[x+1] =='j':
				count -= 1

			if getstr[x] == 'n' and getstr[x+1] =='j':
				count -= 1	

		if len(getstr.strip()) == 2:
			if getstr[x] == '=' or getstr[x] == '-':
				count -= 1
			if getstr[x] == 'l' and getstr[x+1] =='j':
				count -= 1

			if getstr[x] == 'n' and getstr[x+1] =='j':
				count -= 1


	return count-2

print(count_char(input()))

