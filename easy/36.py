#!/usr/bin/python


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        h = {}
        for i in xrange(9):
            for j in xrange(9):
                a = 'row%d %s' % (i, board[i][j])
                b = 'col%d %s' % (j, board[i][j])
                c = 'box%d %s' % ((i/3)*3+j/3, board[i][j])
                if board[i][j] != '.':
                    if a in h or b in h or c in h:
                        return False
                    else:
                        h[a] = True
                        h[b] = True
                        h[c] = True
        return True

x = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
s = Solution()
print s.isValidSudoku(x)
