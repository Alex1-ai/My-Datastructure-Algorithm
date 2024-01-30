def twoSum(nums, target):
    # Create a dictionary to store the values and their indices
    num_indices = {}

    for i, num in enumerate(nums):
        print("index ",i,"num", num)
        complement = target - num
        # Check if the complement exists in the dictionary
        if complement in num_indices:
            # If found, return the indices of the two numbers
            return [num_indices[complement], i]
        # Otherwise, add the current number and its index to the dictionary
        num_indices[num] = i

    # If no solution is found, return an empty list or raise an exception
    return []

# Example usage:
nums1 = [2, 7, 11, 15]
target1 = 9
print(twoSum(nums1, target1))  # Output: [0, 1]

# nums2 = [3, 2, 4]
# target2 = 6
# print(twoSum(nums2, target2))  # Output: [1, 2]

# nums3 = [3, 3]
# target3 = 6
# print(twoSum(nums3, target3))  # Output: [0, 1]

