not_self_num = [0]
for x in range(1,10000):
	i_1 = int(x/1000)
	i_2 = int((x-i_1*1000)/100)
	i_3 = int((x-i_1*1000-i_2*100)/10)
	i_4 = x - i_1*1000 - i_2*100 - i_3*10

	i = x+i_1 + i_2 + i_3 + i_4

	not_self_num.append(i)

for y in range(1,10000):
	if y in not_self_num:
		continue
	else:
		print(y)
	