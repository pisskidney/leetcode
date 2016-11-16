#!/usr/bin/python


class Solution(object):
    def plusOne(self, digits):
        carry = True
        i = len(digits) - 1
        while carry and i >= 0:
            digits[i] += 1
            digits[i] %= 10
            if digits[i] != 0:
                carry = False
            i -= 1
        if carry:
            digits = [1] + digits
        return digits


