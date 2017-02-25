#!/usr/bin/python


maxint = 10**6


class Dijkstra1():
    ''' Adjaciency matrix representation'''
    def shortest_path(self, adj, start, end):
        visited = {start: True}
        A = [maxint for _ in xrange(len(adj))]
        A[start] = 0
        while True:
            next_node = None
            smallest_cost = maxint
            for v in visited:
                for u in xrange(len(adj[0])):
                    if adj[v][u] != -1 and v != u and u not in visited and A[v] + adj[v][u] < smallest_cost:
                        smallest_cost = A[v] + adj[v][u]
                        next_node = u
            if not next_node:
                return -1
            A[next_node] = smallest_cost
            visited[next_node] = True
            if next_node == end:
                return smallest_cost


adj = [
    [0, 1, 4, -1],
    [-1, 0, 2, 6],
    [-1, -1, 0, 3],
    [-1, -1, -1, 0],
]
d = Dijkstra1()
print d.shortest_path(adj, 0, 3)
print d.shortest_path(adj, 3, 0)


class Vertex():
    def __init__(self, nr):
        self.nr = nr
        self.out = []
        self.dist = []
    def __repr__(self):
        return str(self.nr)


vs = []
for i in xrange(4):
    vs.append(Vertex(i))
vs[0].out.extend([vs[1], vs[2]])
vs[0].dist.extend([1, 4])
vs[1].out.extend([vs[2], vs[3]])
vs[1].dist.extend([2, 6])
vs[2].out.extend([vs[3]])
vs[2].dist.extend([3])

class Dijkstra2():
    ''' Adjaciency list representation'''
    def shortest_path(self, start, end):
        from collections import defaultdict
        visited = {start: True}
        A, A[start] = defaultdict(lambda: maxint), 0
        while True:
            shortest_current_path = maxint
            closest_current_vertex = None
            for v in visited:
                for i in xrange(len(v.out)):
                    u = v.out[i]
                    dist_vu = v.dist[i]
                    if u not in visited and dist_vu + A[v] < shortest_current_path:
                        shortest_current_path = dist_vu + A[v]
                        closest_current_vertex = u
            A[closest_current_vertex] = shortest_current_path
            visited[closest_current_vertex] = True
            if closest_current_vertex == end:
                return A[end]

        return -1


d2 = Dijkstra2()
print d2.shortest_path(vs[0], vs[3])


class Dijkstra2():
    def shortest_path(self, vertices, start, end):
        import heapq

        # The hashtable containing the single shource shortest paths
        a = {v: maxint for v in vertices}
        a[start] = 0

        # Initialize priority queue (min-heap)
        prioq = []
        for i in xrange(len(start.out)):
            heapq.heappush(prioq, (start.dist[i], start.out[i]))
        for v in vertices:
            heapq.heappush(prioq, (maxint, v))

        # Start Dijkstra algorithm
        visited = {start: True}
        while prioq:
            dist, w = heapq.heappop(prioq)
            a[w] = dist
            visited[w] = True
            for i in xrange(len(w.out)):






        
        














