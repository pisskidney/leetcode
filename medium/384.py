#!/usr/bin/python


from random import randint
class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type size: int
        """
        self.nums = nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        array = self.nums[:]
        for i in xrange(len(array)):
            rand = randint(i, len(array)-1)
            array[i], array[rand] = array[rand], array[i]
        return array
