class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if (ord(c) == ord('(') or
                ord(c) == ord('[') or
                ord(c) == ord('{')):
                stack.append(c)
            if ord(c) == ord(')'):
                #popped = stack.pop()
                if not stack or ord(stack.pop()) != ord('('): return False
            if ord(c) == ord(']'):
                #popped = stack.pop()
                if not stack or ord(stack.pop()) != ord('['): return False
            if ord(c) == ord('}'):
                #popped = stack.pop()
                if not stack or ord(stack.pop()) != ord('{'): return False
        return not stack