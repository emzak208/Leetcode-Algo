class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        index_to_remove = set() # keep track of ")" to be removed
        stack = [] # keep track of "(" to be removed

        for i, c in enumerate(s):
            if c not in "()":
                continue 
            
            if c == "(":
                stack.append(i)
            elif not stack: 
                index_to_remove.add(i)
            else: 
                stack.pop() # remove the top of stack
        
        # combine all "(" & ")" to be removed
        index_to_remove = index_to_remove.union(set(stack)) 
        string_builder = []
        for i, c in enumerate(s):
            if i not in index_to_remove:
                string_builder.append(c)
        
        return "".join(string_builder)
            




        