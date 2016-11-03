#!/usr/bin/python


class Heap:
    def heapify(self, A, i):
        left, right = -2**32, -2**32
        if len(A) > 2*i+1:
            left = A[2*i+1]
        if len(A) > 2*i+2:
            right = A[2*i+2]
        if left >= right and left > A[i]:
            A[i], A[2*i+1] = A[2*i+1], A[i]
            if (2*i+1) <= len(A)/2:
                self.heapify(A, 2*i+1)
        elif right > left and right > A[i]:
            A[i], A[2*i+2] = A[2*i+2], A[i]
            if (2*i+2) <= len(A) / 2:
                self.heapify(A, 2*i+2)

    def build_heap(self, A):
        n = len(A)
        for i in xrange(n/2, -1, -1):
            self.heapify(A, i)

    def remove_max(self, A):
        if len(A) >= 2:
            A[0], A[-1] = A[-1], A[0]
            res = A.pop()
            i = 0
            while ((2*i+1 < len(A) and A[2*i+1] > A[i]) or
                   (2*i+2 < len(A) and A[2*i+2] > A[i])):
                if A[2*i+1] > A[i] and (2*i+2 >= len(A) or A[2*i+2] <= A[2*i+1]):
                    A[i], A[2*i+1] =A[2*i+1], A[i]
                    i = 2*i+1
                else:
                    A[i], A[2*i+2] =A[2*i+2], A[i]
                    i = 2*i+2
        else:
            return A.pop()
        return res



A = [4, 2, 1, 7, 3, 10, 6, 9, 5, 8]
h = Heap()
print A
h.build_heap(A)
print A
print h.remove_max(A)
print h.remove_max(A)
print h.remove_max(A)
print h.remove_max(A)
print h.remove_max(A)
print h.remove_max(A)
print h.remove_max(A)
print h.remove_max(A)
print h.remove_max(A)
print h.remove_max(A)
