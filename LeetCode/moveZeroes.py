class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """


        # AMATUER 
          # Initialize two pointers
        left, right = 0, 0
        
        # Iterate through the array
        while right < len(nums):
            # If the current element is non-zero, swap it with the left pointer
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            # Move the right pointer to the next element
            right += 1

        if  len(nums)  == 1 or len(nums)==0:
            return nums
        
        for i in range(0, nums.count(0)):
            # print(i)
            nums.remove(0)
            nums.append(0)
        

        # nums.remove(0)
        # nums.append(0)
        # nums.remove(0)
        # nums.append(0)
        
        # print(nums)   
             


result = Solution()
print(result.moveZeroes([0,1,0,3,12]))
print(result.moveZeroes([0]))