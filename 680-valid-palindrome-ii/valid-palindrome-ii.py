class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Method 1: brute force, TLE!
        # step = 0

        # for i in range(len(s)):
        #     new_s = s[0:i] + s[i+1:]
        #     print(i, ': ', new_s)
        #     if new_s == new_s[::-1]:
        #         step += 1 
        #         return True

        # Method 2: Two pointers 
        def check_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True 
        
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return check_palindrome(s, i, j-1) or check_palindrome(s, i + 1, j)
            i += 1 
            j -= 1 
        
        return True




        