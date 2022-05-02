class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
#         if len(cards) == 0:
#             return -1
        
#         min_len = len(cards) + 1
#         for i in range(len(cards)):
#             for j in range(len(cards) - i - 1):
#                 if cards[i] == cards[i + j + 1]:
#                     len_diff = j + 2
#                     min_len = min(min_len, len_diff)
                    
#         if min_len == len(cards) + 1:
#             return -1
#         else:
#             return min_len
                    
        min_len = 10e5
        min_idx_dict = dict()
        
        for i, c in enumerate(cards):
            if c in min_idx_dict:
                len_diff = i - min_idx_dict[c] + 1
                min_len = min(min_len, len_diff)
            min_idx_dict[c] = i
            
        return min_len if min_len != 10e5 else -1
            
        