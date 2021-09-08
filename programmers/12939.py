def solution(s):
	return f'{min(map(int,s.split()))} {max(map(int,s.split()))}'


print(solution("-1 -2 -3 -4"))