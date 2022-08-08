# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

from collections import deque

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        queue = deque(nestedList)
        
        depth = 1
        max_depth = 0
        sum_elements = 0
        sum_products = 0
        
        
        while queue:
            original_len = len(queue)
            max_depth = max(max_depth, depth)
            
            for i in range(original_len):
                nested = queue.pop()
                if nested.isInteger():
                    sum_elements += nested.getInteger()
                    sum_products += depth * nested.getInteger()
                else:
                    queue.extendleft(nested.getList())
            depth += 1 
            
        res = (max_depth + 1) * sum_elements - sum_products
        return res
        
        
        
        