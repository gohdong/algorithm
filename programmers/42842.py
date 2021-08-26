def solution(brown, yellow):
    y = [int((brown-4 + ((4-brown)**2 - 4*2*2*yellow)**0.5) // 4), int((brown-4 - ((4-brown)**2 - 4*2*2*yellow)**0.5)//4)]

    return [max(y) + 2, (yellow // max(y)) + 2]