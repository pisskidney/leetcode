"""
127. Word Ladder

https://leetcode.com/problems/word-ladder/
"""
import string
from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set([endWord])
        q = deque([endWord])
        words = set(wordList)
        res = {endWord: 1}
        if endWord not in words:
            return 0
        while q:
            current = q.popleft()
            for i in range(len(current)):
                for c in string.ascii_lowercase:
                    new_word = current[:i] + c + current[i+1:]
                    if new_word not in visited and (new_word in words or new_word == beginWord):
                        q.append(new_word)
                        res[new_word] = res[current] + 1
                        visited.add(new_word)
                    if new_word == beginWord:
                        return res[new_word]
        return 0


def main():
    s = Solution()
    print(s.ladderLength(
        'hit', 'cog',
        ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
    ))


if __name__ == '__main__':
    raise(SystemExit(main()))
