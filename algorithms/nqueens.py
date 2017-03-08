#!/usr/bin/python


'''
Print all the ways you can fit n queens onto a nxn chess board
'''

c = 0


def nqueens(n):
    solve([], n)
    

def solve(sol, n):
    if len(sol) == n:
        global c
        c += 1
        show(sol)
        return
    for i in xrange(n):
        if noattacks(sol + [i]):
            sol.append(i)
            solve(sol, n)
            sol.pop()


def noattacks(board):
    if len(set(board)) < len(board):
        return False
    for i in xrange(len(board)):
        for j in xrange(i + 1, len(board)):
            if abs(i-j) == abs(board[i]-board[j]):
                return False
    return True


def show(sol):
    row = ['.' for _ in xrange(len(sol))]
    for i in xrange(len(sol)):
        row[sol[i]] = 'Q'
        print ''.join(row)
        row[sol[i]] = '.'
    print '-' * 20


nqueens(8)
print c

