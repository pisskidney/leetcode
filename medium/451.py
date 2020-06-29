# Given a string, sort it in decreasing order based on the frequency of characters.


class Solution:
    def frequencySort(self, s: str) -> str:
        res = []
        chars = [[0, i] for i in range(100)]
        for c in s:
            chars[ord(c) - 48][0] += 1
        chars = sorted(chars, key=lambda x: x[0], reverse=True)
        for c in chars:
            if c[0] > 0:
                res.append(chr(c[2] + 48) * c[0])
            else:
                break
        return ''.join(res)
