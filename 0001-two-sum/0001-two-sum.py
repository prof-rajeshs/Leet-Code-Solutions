class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Dictionary to store the number and its corresponding index
        num_to_index = {}
        
        for index, num in enumerate(nums):
            # Calculate the required number to reach the target
            complement = target - num
            
            # Check if the complement already exists in the dictionary
            if complement in num_to_index:
                return [num_to_index[complement], index]
            
            # Store the current number and its index in the dictionary
            num_to_index[num] = index
            
        return []
