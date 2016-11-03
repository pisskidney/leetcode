#!/usr/bin/python


class Solution(object):
    def reconstructQueue(self, people):
        print people
        people = sorted(people, key=lambda x: x[1])
        print people
        people = sorted(people, key=lambda x: -x[0])
        print people
        res = []
        for p in people:
            res.insert(p[1], p)
        return res


class SolutionDumb(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        people = sorted(people, key = lambda x: x[0])
        for i in xrange(len(people)):
            found = False
            j = i
            while not found and j >= 0:
                for p in people:
                    if p[1] == j:
                        taller = 0
                        for r in res:
                            if r[0] >= p[0]:
                                taller += 1
                        if taller == p[1]:
                            people.remove(p)
                            res.append(p)
                            found = True
                            break
                j -= 1
        return res


s = Solution()
x = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print s.reconstructQueue(x)
                


