def max_sum_array_k(data, k):
    left = 0
    max_length = float('-inf')
    array_sum  = 0

    for right in range(len(data)):
        array_sum += data[right]

        while right - left + 1 == k:
            max_length = max(max_length, array_sum)
            array_sum -= data[left]
            left += 1



    return max_length



nums = [2, 3, 4, 1, 5]
k = 2

answer = max_sum_array_k(nums, k)

print(answer)
