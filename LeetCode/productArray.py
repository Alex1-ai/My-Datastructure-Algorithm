"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 



"""

class Solution(object):
    def productExceptSelf(self,nums):
        n = len(nums)
        
        # Initialize left and right arrays
        left, right = [1] * n, [1] * n
        
        # Compute left products
        product = 1
        for i in range(1, n):
            product *= nums[i - 1]
            left[i] = product
        
        # Compute right products
        product = 1
        for i in range(n - 2, -1, -1):
            product *= nums[i + 1]
            right[i] = product
        
        # Compute final result
        result = [left[i] * right[i] for i in range(n)]
        
        return result

        
        



result = Solution()
print(result.productExceptSelf([1,2,3,4,]))
print(result.productExceptSelf([-1,1,0,-3,3]))