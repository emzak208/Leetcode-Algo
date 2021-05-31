# 思路： 
# 1. 一棵拥有n个节点的树有n-1条边，树是连通的，没有环的。
# 2. 给定一个无向图让我们判断是否为树，我们只需要判断是否连通且无环即可。
# 3. 我们可以从根节点出发向儿子节点进行广度优先搜索bfs，如果能遍历完所有的点，且没有环存在，那么说明这个无向图是树。
# 4. 已知给定的边不重复，所以可以通过判断边数是否为(n - 1)条来判断是否无环。


from collections import deque 

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0 or len(edges) != n - 1: # edges为空是TRUE，因此不能加在这里
            return False 
        
        # new_edges里存edges里所有的[start,end],以及他们的reverse[end,start]
        # 如果只存正序没有倒序，当给的edges是倒序时，就不满足start = node， bfs就会跳过造成错误结果
        new_edges = []
        for start, end in edges:
            new_edges.append([start,end])
            new_edges.append([end,start])
            
        queue = deque([0])
        visited = set([0])
        
        while queue: 
            node = queue.popleft()
            for start, end in new_edges:
                if start == node and end not in visited:
                    queue.append(end)
                    visited.add(end)
         
        # 最后判断是否有环
        if len(visited) == n:
            return True 
        return False
            
        