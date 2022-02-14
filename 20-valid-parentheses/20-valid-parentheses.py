class Solution:
    def isValid(self, s: str) -> bool:
        par_dict = {')':'(',
                    ']':'[',
                    '}':'{'}        

        stack = []
        
        for char in s: 
            if char in par_dict: 
                top_element = stack.pop() if stack else '#'
                if top_element != par_dict[char]:
                    return False
            
            else:
                stack.append(char)
        
        if len(stack) == 0:
            return True
        else: 
            return False 
                
                
                
#  [()()]
# reverse = ])()([
# 最后看到的线close 
# [(a + b) + (c + d)]