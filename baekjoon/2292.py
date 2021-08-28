# def an(n):
# 	if n<=0:
# 		return 0
# 	return n+an(n-1)

# def an(n):
# 	a=0
# 	for i in range(n):
# 		a+=i
# 	return a

# def bee_house(getint):
# 	n=0
# 	if int(getint) == 1:
# 		return 1

# 	else:
# 		while True:
# 			if int(6*an(n)+2)<=int(getint)<int(6*an(n+1)+2):
# 				return n+1
# 				break
# 			n+=1

def bee_house(getint):

	left=0
	right=6
	step = 6
	n = 1
	if getint == 1:
		return n

	while True:
		# print(left , right)
		if left+2<= getint < right+2:
			return n+1
			break

		n+=1
		step+=6
		left+=step-6
		right+=step




# for x in range(10000):
# 	if x==0:
# 		print(0)
# 	else:
# 		print(bee_house(x))

b=int(input())
if b <= 0:
	print(0)
else:
	print(int(bee_house(b)))

# print(an(int(input())))