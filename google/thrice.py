#!/usr/bin/python


'''
Given a sequence of integers, get the nr that only appears twice and not thrice.
eg: 11122233444555 -> 3
'''


def solve(A):
    n = (len(A) + 1)/3 
    return (3*n*(n+1))/2 - sum(A)


A1 = [1,1,1,2,2,3,3,3,4,4,4]
A2 = [1,1]
A3 = [1,1,1,2,2,2,3,3,3,4,4]
print solve(A1)
print solve(A2)
print solve(A3)
