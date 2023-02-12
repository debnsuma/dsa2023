'''
Problem:
https://leetcode.com/problems/concatenation-of-array/

'''

def getConcatenation(nums):
    n = len(nums)
    ans = []
    for i in range(2*n):
        if i < n:
            ans.append(nums[i])
        else:
            ans.append(nums[i-n])
    
    return ans

nums = [1,3,2,1]
getConcatenation(nums)