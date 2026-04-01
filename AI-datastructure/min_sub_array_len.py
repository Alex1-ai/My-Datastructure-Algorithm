def minSubArrayLen(data, target):
    min_length = float('inf')
    left = 0
    window_sum = 0

    for right in range(len(data)):
        window_sum += data[right]

        while window_sum >= target:
            min_length = min(min_length, (right - left + 1))
            window_sum -= data[left]
            left+=1

    return 0 if min_length == float('inf') else min_length











target = 7
nums = [2,3,1,2,4,3]

answer = minSubArrayLen(nums, target)

print(answer)
