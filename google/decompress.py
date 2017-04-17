#!/usr/bin/python


'''
Given a string where each number denotes the number of times the string
in [] appears, decompress it.
eg: a3[b2[c1[d]]]e will be decompressed as abcdcdbcdcdbcdcde
'''


def solve(S, n):
    if '[' in S and ']' in S:
        left = 0
        while S[left] != '[':
            left += 1
        right = len(S) - 1
        while S[right] != ']':
            right -= 1
        m = int(S[left-1])
        return n * (S[:left-1] + solve(S[left+1:right], m) + S[right+1:])
    return S * n
    

S = 'a3[b2[c1[d]]]e'
print solve(S, 1)
assert solve(S,1) == 'abcdcdbcdcdbcdcde'
