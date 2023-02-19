class Solution:
    def twoSum(self, nums, target):
        nums_seen = dict()
        
        for i in range(len(nums)):
            present_element = nums[i]
            if target - present_element in nums_seen:
                return nums_seen[target - present_element], i 
            elif present_element not in nums_seen:
                nums_seen[present_element] = i 
                    
        return False