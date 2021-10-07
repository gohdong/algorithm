def solution(s):
    s = s.lower()
    for i,x in enumerate(s):
        if i == 0 or s[i-1] == ' ':
            s = s[:i] + s[i].upper() + s[i+1:]
        
    return s