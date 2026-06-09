
class Solution:
    def isValid(self, s: str) -> bool:
        matches={'(':')','[':']','{':'}'}
       
        stack=deque()
        for char in s[::-1]:
            if char in matches.values():
                stack.append(char)
            else:
                if not stack:
                    return False
                top=stack[-1]
                if matches[char]==top:
                    stack.pop()
                else:
                    return False
        return len(stack)==0

        