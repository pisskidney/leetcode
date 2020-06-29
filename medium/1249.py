# Given a string s of '(' , ')' and lowercase English characters. 
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        i = 0
        res = ''
        for c in s:
            if c == '(':
                stack.append(1)
                res += c
            elif c == ')':
                if stack:
                    stack.pop()
                    res += c
            else:
                res += c
        final = ''
        stack = []
        for i in range(len(res)-1, -1, -1):
            if res[i] == ')':
                stack.append(1)
                final = res[i] + final
            elif res[i] == '(':
                if stack:
                    stack.pop()
                    final = res[i] + final
            else:
                final = res[i] + final
        return final


s = Solution()
print(s.minRemoveToMakeValid('t)e(st)te(st'))
