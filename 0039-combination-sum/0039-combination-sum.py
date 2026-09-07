from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(remain, combo, start):
            # Base case: valid combination found
            if remain == 0:
                res.append(list(combo))
                return
            # Base case: exceeded the target sum
            elif remain < 0:
                return
            
            for i in range(start, len(candidates)):
                # Include the candidate in the current combination
                combo.append(candidates[i])
                # Reuse the same element by keeping the start index as i
                backtrack(remain - candidates[i], combo, i)
                # Backtrack by removing the last added element
                combo.pop()
                
        backtrack(target, [], 0)
        return res