from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(path, used):
            # If the current permutation is complete, add it to the results
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                # Skip if the element is already included in the current path
                if used[i]:
                    continue
                
                # Make a choice
                used[i] = True
                path.append(nums[i])
                
                # Recurse
                backtrack(path, used)
                
                # Undo the choice (backtrack)
                path.pop()
                used[i] = False
                
        backtrack([], [False] * len(nums))
        return res
