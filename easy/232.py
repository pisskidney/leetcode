#!/usr/bin/python


class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.revstack = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        x = self.stack[:]
        self.revstack = []
        while x:
            self.revstack.append(x.pop())

    def pop(self):
        """
        :rtype: nothing
        """
        self.revstack.pop()
        x = self.revstack[:]
        self.stack = []
        while x:
            self.stack.append(x.pop())
        
    def peek(self):
        """
        :rtype: int
        """
        return self.revstack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not bool(self.stack)


q = Queue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)
print q.stack, q.revstack
print q.peek()
q.pop()
q.pop()
q.pop()
q.pop()
print q.stack, q.revstack, q.empty()
