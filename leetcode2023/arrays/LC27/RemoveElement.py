'''
Problem :
https://leetcode.com/problems/remove-element/

'''

def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] == val:
            continue
        else:
            nums[k] = nums[i]
            k += 1
    
    # print(nums, k)
    return k


nums = [0,1,2,2,3,0,4,2]
val = 2
removeElement(nums, val)

