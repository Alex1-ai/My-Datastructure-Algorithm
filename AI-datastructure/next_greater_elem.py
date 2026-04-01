# def next_greater(nums):
#     stack = []
#     result = [-1] * len(nums)

#     for i in range(len(nums) - 1, -1, -1):
#         # Remove smaller elements
#         print("stack", stack)
#         while stack and stack[-1] <= nums[i]:
#             print("result ",result)
#             stack.pop()

#         # If stack not empty → next greater exists
#         if stack:
#             result[i] = stack[-1]
#             print("result", result)

#         print("stack", stack)
#         # Push current element
#         stack.append(nums[i])

#     return result



















def next_greater(nums):
    stack = []
    result = [-1] * len(nums)

    for i in range(len(nums) -1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()




        if stack:
           result[i] = stack[-1]

        stack.append(nums[i])

    return result


data = [2, 1, 2, 4, 3]
answer = next_greater(data)
print(answer)
