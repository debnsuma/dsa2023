
'''

Problem Detials: 
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

'''

def removeDuplicates(nums):
    k = 1
    last_seen = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == last_seen:
            pass 
        else:
            last_seen = nums[i]
            nums[k] = nums[i]
            k += 1
    
    # print(nums)
    # print(k)
    return k

nums = [0,0,1,1,1,2,2,3,3,4]
removeDuplicates(nums)

nums = [1,1,2]
removeDuplicates(nums)
