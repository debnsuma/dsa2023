class Solution:
    def productExceptSelf(self, nums):
        
        result  = [1] * len(nums)
        current_product = 1

        # Left Product 
        for i in range(len(nums)):
            result[i] = current_product * result[i]
            current_product *= nums[i]
            
        
        # Right Product
        current_product = 1 
        for i in range(len(nums) - 1, -1, -1):
            result[i] = current_product * result[i]
            current_product *= nums[i]
            

        return result     
