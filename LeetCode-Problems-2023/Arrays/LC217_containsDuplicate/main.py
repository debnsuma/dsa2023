class Solution:
    def containsDuplicate(self, nums):
        nums_seen = {}

        for num in nums:
            if num not in nums_seen:
                nums_seen[num] = True
            else:
                return True

        return False 
