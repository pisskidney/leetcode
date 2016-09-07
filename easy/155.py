#!/usr/bin/python


class MinStack(object):

    def __init__(self):
        self.data = []
        self.mins = []
        self.minint = None
        self.minindex = None
        

    def push(self, x):
        oldmin = None
        if not self.data:
            self.minint = x
            self.minindex = 0
        else:
            if x <= self.minint:
                self.minint = x
                oldmin = self.minindex
                self.minindex = len(self.data)
        
        self.data.append(x)
        self.mins.append(oldmin)
        
        
    def pop(self):
        if self.data:
            if self.mins[-1] is not None:
                self.minint = self.data[self.mins[-1]]
                self.minindex = self.mins[-1]
                
            self.mins.pop()
            return self.data.pop()
        

    def top(self):
        if self.data:
            return self.data[-1]
        

    def getMin(self):
        return self.minint


s = MinStack()
s.push(2)
s.push(7)
s.push(20)
s.push(1)
s.push(0)
s.pop()
assert s.getMin() == 1
s.pop()
assert s.getMin() == 2

s.pop()
s.pop()
s.push(2)
s.push(2)
s.push(0)
assert s.getMin() == 0
s.pop()
assert s.getMin() == 2
s.pop()
s.pop()
assert s.getMin() == 2
