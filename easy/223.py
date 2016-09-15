#!/usr/bin/python


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        common = 0
        if max(A, E) < min(C, G) and max(B, F) < min(D, H):
            common = (min(C, G) - max(A, E)) * (min(D, H) - max(B, F))
        return (C - A) * (D - B) + (G - E) * (H - F) - common
