# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        columnTable = defaultdict(list)
        queue = deque([(root, 0)]) # tuple 
        
        while queue: 
            node, col_ind = queue.popleft()
            
            if node is not None:
                columnTable[col_ind].append(node.val)
                
                queue.append((node.left, col_ind - 1))
                queue.append((node.right, col_ind + 1))
                
        return [columnTable[x] for x in sorted(columnTable.keys())] # for all the pairs in the dictionary, sort the pairs by key, aka column index to insure left to right order
                        
        
        # {0:[2], => {-1:[9,11],0:[2],1:[8,5]} # first order by column, then order by row, where row order is handled by BFS intrinsictly 
        #  -1:[9],
        #  1:[8]} 