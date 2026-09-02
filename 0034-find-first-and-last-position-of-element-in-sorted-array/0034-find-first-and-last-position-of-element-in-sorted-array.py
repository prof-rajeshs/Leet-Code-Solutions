class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findBound(isFirst: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    bound = mid
                    if isFirst:
                        right = mid - 1  # Keep searching left
                    else:
                        left = mid + 1   # Keep searching right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return bound

        first = findBound(True)
        if first == -1:
            return [-1, -1]
        
        last = findBound(False)
        return [first, last]