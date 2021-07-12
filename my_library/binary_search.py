def solution(n_list, target):
    left = 0
    right = len(n_list) - 1
    mid = 0
    while left <= right:
        mid = (left + right) // 2

        if mid == left or mid == right:
            break

        if n_list[mid] < target:
            right = mid - 1
        else:
            left = mid + 1

    return mid


print(solution([50, 60, 100, 120, 250, 260], 60))
