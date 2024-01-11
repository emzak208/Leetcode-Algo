"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # Method 1 : naive approqach 
        # seen = set()

        # while p: 
        #     seen.add(p)

        #     p = p.parent 

        # while q: 
        #     if q in seen:
        #         return q

        #     q = q.parent

        # Method 2: brillaint solution, need to memorise 
        p_copy = p
        q_copy = q
        
        # if p_copy == q_copy:
        #     return p_copy

        while p_copy != q_copy:
            p_copy = p_copy.parent
            q_copy = q_copy.parent

            if p_copy is None:
                p_copy = q
            if q_copy is None:
                q_copy = p

        return p_copy

        












