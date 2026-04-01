def sub_arrays(data, k):
    window_sum = 0
    max_sum = 0
    left = 0

    for right in range(len(data)):
        window_sum += data[right]

        if right - left + 1 == k:
           max_sum = max(window_sum, max_sum)
           window_sum -= data[left]

           left+=1
    return max_sum


nums = [2, 1, 5, 1, 3, 2]
k = 3

answer = sub_arrays(nums, k)
print(answer)
