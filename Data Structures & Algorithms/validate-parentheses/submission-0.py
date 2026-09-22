class Solution:
    def isValid(self, s: str) -> bool:
        complement = {'}':'{', ']':'[', ')': '('}
        stack = []
        for ch in s:
            if len(stack) > 0 and complement.get(ch, 0) == stack[-1]:
                stack.pop()
                continue
            stack.append(ch)
        if len(stack) != 0:
            return False
        return True