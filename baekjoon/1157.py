a = input().upper()
b = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for x in a:
	b[ord(x)-65] +=1

max_num = b[0]
max_loc = 0
for x in range(1,26):
	if b[x]>= max_num:
		max_num = b[x]
		max_loc = x


max_count = 0
for x in range(26):
	if b[x] == max_num:
		max_count+=1

if max_count ==1:
	print(chr(max_loc+65))
else:
	print("?")