def solution(n, k, cmd):
    answer = ''

    max_index = n - 1
    next_index = k
    before_index = 0
    deleted_stack = []

    default_table = ["O" for _ in range(n)]

    for c in cmd:
        # print("=====", c, "=====")
        # print(default_table)
        before_index = next_index
        # print(before_index)
        if c[0] == "D":
            next_index += int(c[2])

        if c[0] == "U":
            next_index -= int(c[2])

        if c[0] == "C":
            # print(before_index)

            default_table[before_index] = "X"
            deleted_stack.append(before_index)
            if before_index != max_index:
                next_index += 1
            else:
                max_index = before_index - 1
                next_index = max_index

        if c[0] == "Z":
            temp = deleted_stack.pop()
            if temp > max_index:
                max_index = temp
            default_table[temp] = "O"

        if before_index < next_index:
            will_go = next_index - before_index
            while will_go > 0:
                before_index += 1

            temp = default_table[before_index + 1:next_index + 1].count("X")
            next_index += temp
        if next_index < before_index:
            # print(default_table[next_index :before_index + 1])
            next_index -= default_table[next_index:before_index].count("X")
            # print(next_index, before_index + 1, default_table[next_index:before_index + 1])
        if next_index > max_index:
            next_index = max_index
        if next_index < 0:
            next_index = 0
        # print(next_index)
        # print(default_table)
        # print("===============")

    return "".join(default_table)


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
