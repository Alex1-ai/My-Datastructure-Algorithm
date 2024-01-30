

def merge_sort(arr):
    if len(arr) <= 1:
        print("Entered here ", arr)
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    print("split array into two")

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    print("recurssion here")

    # Merge the sorted halves
    sorted_arr = merge(left_half, right_half)
    print("reached here")

    return sorted_arr

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        print("merge ", left , right)
        print("left ",left)
        print("right ", right)
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Example usage:
arr = [8, 3, 2, 9, 1, 39, 8, 2, 20, 38, 10, 12, 14]
sorted_arr = merge_sort(arr)
print(sorted_arr)



