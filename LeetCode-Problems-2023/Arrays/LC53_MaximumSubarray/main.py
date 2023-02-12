'''
Problem:
https://leetcode.com/problems/maximum-subarray/

'''

def maxSubArray(nums):

    max_sum = nums[0]
    current_sum = 0
    for i in nums:
        current_sum = current_sum + i 
        current_sum = max(current_sum, i)
        max_sum = max(max_sum, current_sum)
        # print(i, current_sum, max_sum)
        # print("***********************")

    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
maxSubArray(nums)