# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
# class Solution:
#     def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root:
#             return []
        
#         queue = [root]
#         result = [[root.val]]
        
#         isForward = -1 
#         while queue:
#             next_queue = []
#             for node in queue:
#                 if node.left:
#                     next_queue.append(node.left)
#                 if node.right:
#                     next_queue.append(node.right)
#             result.append(node.val for node in next_queue[::isForward])
#             queue = next_queue 
#             isForward *= -1
#         del result[-1]
#         return result 
    
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = collections.deque()
        q.append(root)
        #正反向标志
        isForward = 1
        while len(q) is not 0:
            row = []
            for i in range(len(q)):
                if q[0].left:
                    q.append(q[0].left)
                if q[0].right:
                    q.append(q[0].right)
                row.append(q[0].val)
                q.popleft()
            #根据标志来确认当前层遍历的方向
            row = row[::isForward]#翻转
            ans += [row]
            #方向反转
            isForward *= -1
        return ans

        
