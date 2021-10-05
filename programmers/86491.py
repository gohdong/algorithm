def solution(sizes):
    h = 0
    w = 0
    for size in sizes:
        if size[0] > size[1]:
            h = max(h,size[0])
            w = max(w,size[1])
            
        else:
            h = max(h,size[1])
            w = max(w,size[0])
    
    return h*w


print(solution())