def solution(n):
    return "수박" * (n//2) if not n%2 else "수박" * (n//2) + "수"

print(solution())