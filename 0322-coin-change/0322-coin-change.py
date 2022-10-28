from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = deque([(amount, 0)])
        seen = set([amount])
        
        while q: 
            remainingAmount, numCoins = q.popleft()
            if remainingAmount == 0:
                return numCoins
            
            for coin in coins:
                subAmount = remainingAmount - coin
                if subAmount >=0 and subAmount not in seen:
                    q.append((subAmount, numCoins + 1)) # queue use append
                    seen.add(subAmount) # set use add
                    
        return -1