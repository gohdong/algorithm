class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for x in s:
            if x == "(":
                stack.append(x)
            if x == "{":
                stack.append(x)
            if x == "[":
                stack.append(x)
            if not stack:
                return False
            if x == ")":
                temp = stack.pop()
                if temp != "(":
                    stack.append(temp)
                    break
            if x == "}":
                temp = stack.pop()
                if temp != "{":
                    stack.append(temp)
                    break
            if x == "]":
                temp = stack.pop()
                if temp != "[":
                    stack.append(temp)
                    break

        # print(stack)
        if not stack:
            return True

        return False