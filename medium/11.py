class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, n - 1
        res = 0
        while i < j:
            h = min(height[i], height[j])
            vol = (j - i) * h
            res = max(res, vol)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return res


