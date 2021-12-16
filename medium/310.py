"""
310. Minimum Height Trees

https://leetcode.com/problems/minimum-height-trees/
"""
from collections import defaultdict, deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]

        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        def bfs(start):
            distance = {}
            distance[start] = 0
            prev = {start: None}
            q = deque([start])
            while q:
                node = q.popleft()
                for neighbour in adj[node]:
                    if neighbour not in distance:
                        prev[neighbour] = node
                        distance[neighbour] = distance[node] + 1
                        q.append(neighbour)
            maxi, maxd = -1, -1
            for node, dist in distance.items():
                if dist > maxd:
                    maxi = node
                    maxd = dist
            path = []
            q = maxi
            while q is not None:
                path.append(q)
                q = prev[q]
            return maxi, path

        start, _ = bfs(0)
        end, path = bfs(start)

        if len(path) % 2:
            return [path[len(path) // 2]]
        return path[len(path)//2-1:len(path)//2+1]


def main():
    s = Solution()
    print(s.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))


if __name__ == '__main__':
    raise(SystemExit(main()))
