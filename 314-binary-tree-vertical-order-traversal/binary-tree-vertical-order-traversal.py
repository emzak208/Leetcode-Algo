# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        table = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, col_index = queue.popleft()

            if node is not None: 
                table[col_index].append(node.val) # we can have multiple values/nodes for the same column
                queue.append((node.left, col_index - 1))
                queue.append((node.right, col_index + 1))

        return [table[x] for x in sorted(table.keys())]

        