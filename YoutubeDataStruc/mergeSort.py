def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    # divide the array in two part
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    # then merging the 1 arrays element array now
    merge_two_sorted_lists(left, right, arr)


def merge_two_sorted_lists(a, b, arr):

    len_a = len(a)
    len_b = len(b)

    # iterating when you are the last element
    i = j = k = 0
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]

            i += 1

        else:
            arr[k] = b[j]
            j += 1
        k += 1

    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1

    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


if __name__ == '__main__':
    a = [5, 8, 12, 56]
    b = [7, 9, 45, 51]
    arr = [10, 3, 15, 7, 8, 23, 98, 29]

    merge_sort(arr)
    print(arr)
