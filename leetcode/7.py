class Solution:
    def reverse(self, x: int) -> int:
        flag = 1
        answer = "0"




        if x < 0:
            flag = -1

        for i, a in enumerate(str(abs(x))[::-1]):
            if i == 0 and a == "0":
                continue
            answer += a

        a = int(flag * int(answer))
        if -(2**31) > a or a > 2**31-1:
            return 0

        return int(flag * int(answer))
