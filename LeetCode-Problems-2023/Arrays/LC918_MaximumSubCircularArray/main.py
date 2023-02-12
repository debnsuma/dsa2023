'''
Problem:
https://leetcode.com/problems/maximum-sum-circular-subarray

'''

def maxSubarraySumCircular(nums):

    curr_max = nums[0]
    max_so_far = nums[0]

    curr_min = nums[0]
    min_so_far = nums[0]
    nums_2 = nums[1::]
    for i in range(len(nums_2)):
        curr_max = max(curr_max + nums_2[i], nums_2[i]) 
        max_so_far = max(max_so_far, curr_max)

        curr_min = min(curr_min + nums_2[i], nums_2[i])
        min_so_far = min(min_so_far, curr_min)

        print(curr_max, max_so_far, curr_min, min_so_far)

    result = max(max_so_far, sum(nums)-min_so_far) 

    if result == 0:
        return max(nums)
    return result


