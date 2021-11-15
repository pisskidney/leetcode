"""
79. Word Search

https://leetcode.com/problems/word-search/
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def go(visited, i, j, word):
            if not word:
                return True
            if i < 0 or i >= len(board):
                return False
            if j < 0 or j >= len(board[0]):
                return False
            if (i, j) in visited:
                return False

            if board[i][j] == word[0]:
                visited.add((i, j))
                found = (
                    go(visited, i-1, j, word[1:]) or
                    go(visited, i+1, j, word[1:]) or
                    go(visited, i, j-1, word[1:]) or
                    go(visited, i, j+1, word[1:])
                )
                visited.remove((i, j))
                return found
            return False

        n, m = len(board), len(board[0])
        acc = []
        for i in range(n):
            for j in range(m):
                acc.append(go(set([]), i, j, word))
        return any(acc)


def main():
    s = Solution()
    print(s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))


if __name__ == '__main__':
    raise(SystemExit(main()))
