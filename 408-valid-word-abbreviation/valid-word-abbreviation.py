class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0

        # loop through abbr 
        while i < len(abbr): 
            if j >= len(word):
                return False 

            if not abbr[i].isdigit():
                if abbr[i] != word[j]:
                    return False
                i += 1 
                j += 1 
            else:
                # leading 0
                if abbr[i] == '0':
                    return False
                n = ''
                # Find the number 
                while i < len(abbr) and abbr[i].isdigit(): 
                    n += abbr[i]
                    i += 1 
                j += int(n)

        return j == len(word) 


            
                
                 
        